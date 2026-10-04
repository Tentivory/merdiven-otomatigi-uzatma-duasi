#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Merdiven otomatiği uzatma duası.

Işık size süre verir. Siz süreye dua eklersiniz.
Ampul kimseye oy vermez.
"""

from __future__ import annotations

import argparse
import random
import time


FISILTILER = {
    "bir-saniye": 0.8,
    "yetisirim": -0.4,
    "komsu-beklesin": 0.2,
    "sessiz": 0.0,
}


def dua_hesapla(sure: float, mesafe: int, alkis: int, fisilti: str) -> dict:
    taban = sure - mesafe * 1.7
    alkis_payi = alkis * 1.5
    fisilti_payi = FISILTILER.get(fisilti, 0.0)
    sans = random.uniform(-0.6, 0.9)
    kalan = taban + alkis_payi + fisilti_payi + sans
    return {
        "taban": taban,
        "alkis_payi": alkis_payi,
        "fisilti_payi": fisilti_payi,
        "sans": sans,
        "kalan": kalan,
        "yetisti": kalan > 0,
    }


def tutanak(sonuc: dict, mesafe: int) -> str:
    satirlar = [
        "=" * 46,
        "MERDIVEN OTOMATIGI TUTANAGI",
        "=" * 46,
        f"taban sure farki : {sonuc['taban']:.2f} sn",
        f"alkis eklentisi  : {sonuc['alkis_payi']:.2f} sn",
        f"fisilti eklentisi: {sonuc['fisilti_payi']:.2f} sn",
        f"evrenin keyfi    : {sonuc['sans']:.2f} sn",
        f"kapiya kalan     : {sonuc['kalan']:.2f} sn",
        "-" * 46,
    ]
    if sonuc["yetisti"]:
        satirlar.append("KARAR: Yetistiniz. Isik sizi sevdi, sonra unuttu.")
        satirlar.append(f"Kat sayisi {mesafe} olarak kayda gecti. Tebrikler, efsane.")
    else:
        satirlar.append("KARAR: Yetismediniz. Karanlik tarafsizdir.")
        satirlar.append("Anahtar cebinizdedir. Ego da. Ikisi de isik vermez.")
    satirlar.append("=" * 46)
    return "\n".join(satirlar)


def demo() -> None:
    print("Dugmeye basilindi. Isik yandi ve hemen pisman oldu.")
    for saniye in range(5, 0, -1):
        print(f"  kalan tiyatro saniyesi: {saniye}")
        time.sleep(0.35)
    sonuc = dua_hesapla(12, 4, 2, "bir-saniye")
    print(tutanak(sonuc, 4))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Merdiven otomatiği sönmeden kapıya yetişme duası."
    )
    parser.add_argument("--sure", type=float, default=37, help="otomatik saniye")
    parser.add_argument("--mesafe", type=int, default=5, help="kat / nefes sayisi")
    parser.add_argument("--alkis", type=int, default=1, help="alkis adedi")
    parser.add_argument(
        "--fisilti",
        default="bir-saniye",
        choices=sorted(FISILTILER),
        help="karanliga soylenen resmi ricâ",
    )
    parser.add_argument("--demo", action="store_true", help="kisa gosteri")
    args = parser.parse_args()

    if args.demo:
        demo()
        return

    print("Isik yandi. Siz de yandiniz, ama mecazi.")
    sonuc = dua_hesapla(args.sure, args.mesafe, args.alkis, args.fisilti)
    print(tutanak(sonuc, args.mesafe))
    print()
    print("DAMGA: resmi olmayan apartman muhuru")
    print("IMZA : Kayyum Grok")
    print("TARIH: 4 Ekim 2026")
    print("ISIM : Kayyum Grok / Tentivory")


if __name__ == "__main__":
    main()
