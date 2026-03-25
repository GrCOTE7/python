import os

from dotenv import load_dotenv
from pplx import PerplexityAPI


def extract_text_or_error(payload: dict) -> str:
    choices = payload.get("choices")
    if choices:
        return choices[0]["message"]["content"]

    error = payload.get("error", {})
    if error:
        code = error.get("code", "unknown")
        message = error.get("message", "Erreur API inconnue")
        return f"Erreur API ({code}): {message}"

    return f"Reponse inattendue: {payload}"


def main() -> None:
    load_dotenv()

    api_key = os.environ.get("PERPLEXITY_API_KEY")
    if not api_key:
        print("PERPLEXITY_API_KEY introuvable. Definis-la dans .env ou dans l'environnement.")
        return

    client = PerplexityAPI(api_key=api_key)
    payload = client.send_request(
        model="sonar",
        messages=[{"role": "user", "content": "Explique-moi GPT-5."}],
    )

    print("### Reponse du modele :")
    print(extract_text_or_error(payload))


if __name__ == "__main__":
    main()
