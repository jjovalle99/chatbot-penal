import argparse
import os
from typing import List

from bs4 import BeautifulSoup


def get_file_names(path: str) -> List[str]:
    file_names = [file for file in os.listdir(path) if file.endswith(".html")]
    if not file_names:
        raise FileNotFoundError("No hay archivos HTML en el directorio especificado")
    file_names = sorted(file_names, key=lambda x: int(x.split("_")[1].split(".")[0]))
    return file_names


def load_htmls_as_txt(path: str, file_names: List[str]) -> List[str]:
    texts = []
    for file in file_names:
        with open(os.path.join(path, file), "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")
            texts.append(soup.get_text())
    return texts


def clean_data(texts: List[str]) -> List[str]:
    cleaned_texts = []
    for text in texts:
        if texts.index(text) == 0:
            split_patern = "\nSiguiente"
        elif texts.index(text) == len(texts) - 1:
            split_patern = "\nAnterior"
        else:
            split_patern = "\nAnterior | Siguiente"

        split_text = text.split(split_patern)
        if len(split_text) != 3:
            raise ValueError(f"{split_text}")
        cleaned_texts.append(split_text[1].strip())
    return cleaned_texts


def save_texts(cleaned_texts: List[str], output_path: str) -> None:
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    for i, text in enumerate(cleaned_texts, start=1):
        file_name = f"cleaned_output_{i}.txt"
        file_path = os.path.join(output_path, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_path",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output_path",
        type=str,
        required=True,
    )
    args = parser.parse_args()

    try:
        file_names = get_file_names(args.input_path)
        texts = load_htmls_as_txt(args.input_path, file_names)
        cleaned_texts = clean_data(texts)
        save_texts(cleaned_texts, args.output_path)
    except Exception as e:
        print(f"Error: {e}")
