import hashlib

import requests
import webview


class Api:
    def verifica_recebeu(self, senha_usuario):
        if not senha_usuario.strip():
            return "Por favor, digite uma senha antes de verificar."

        senha_hash = hashlib.sha1(senha_usuario.encode("utf-8")).hexdigest().upper()
        prefixo = senha_hash[:5]
        sufixo = senha_hash[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefixo}"

        try:
            resposta = requests.get(url, timeout=10)
            resposta.raise_for_status()
        except requests.RequestException:
            return "Não foi possível consultar o serviço. Tente novamente."

        for linha in resposta.text.splitlines():
            if not linha.strip():
                continue

            sufixo_api, quantidade = linha.split(":", 1)

            if sufixo_api == sufixo:
                return (
                    f"Sua senha apareceu em vazamentos {quantidade} vezes! "
                    "Altere-a imediatamente."
                )

        return "Nenhum vazamento conhecido foi encontrado para essa senha."


if __name__ == "__main__":
    api = Api()

    window = webview.create_window(
        "Password Leak Checker",
        "index.html",
        width=600,
        height=400,
        js_api=api,
    )

    webview.start()
