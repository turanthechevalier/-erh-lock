"""DOCX dosyasını LibreOffice (UNO) ile açar, içindekiler tablosunu günceller
ve PDF olarak dışa aktarır. Kullanım: python3 pdf_cevir.py girdi.docx cikti.pdf
"""
import os
import subprocess
import sys
import time

import uno
from com.sun.star.beans import PropertyValue


def ozellik(ad, deger):
    p = PropertyValue()
    p.Name = ad
    p.Value = deger
    return p


def main():
    girdi = os.path.abspath(sys.argv[1])
    cikti = os.path.abspath(sys.argv[2])
    port = 2002
    profil = "file:///tmp/lo_kitap_profil"
    surec = subprocess.Popen([
        "soffice", "--headless", "--invisible", "--nologo", "--norestore",
        f"-env:UserInstallation={profil}",
        f"--accept=socket,host=127.0.0.1,port={port};urp;",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        yerel = uno.getComponentContext()
        cozucu = yerel.ServiceManager.createInstanceWithContext(
            "com.sun.star.bridge.UnoUrlResolver", yerel)
        baglam = None
        for _ in range(60):
            try:
                baglam = cozucu.resolve(
                    f"uno:socket,host=127.0.0.1,port={port};urp;StarOffice.ComponentContext")
                break
            except Exception:
                time.sleep(1)
        if baglam is None:
            raise SystemExit("LibreOffice'e bağlanılamadı")
        masaustu = baglam.ServiceManager.createInstanceWithContext(
            "com.sun.star.frame.Desktop", baglam)
        belge = masaustu.loadComponentFromURL(
            uno.systemPathToFileUrl(girdi), "_blank", 0, (ozellik("Hidden", True),))
        # Sayfa numaraları yerleşsin diye iki tur güncelle
        for _ in range(2):
            dizinler = belge.getDocumentIndexes()
            for i in range(dizinler.getCount()):
                dizinler.getByIndex(i).update()
            belge.refresh()
        belge.storeToURL(uno.systemPathToFileUrl(cikti),
                         (ozellik("FilterName", "writer_pdf_Export"),))
        # Güncellenmiş içindekilerle DOCX'i de yeniden kaydet
        belge.storeToURL(uno.systemPathToFileUrl(girdi),
                         (ozellik("FilterName", "MS Word 2007 XML"),))
        belge.close(True)
        try:
            masaustu.terminate()
        except Exception:
            pass
    finally:
        time.sleep(1)
        surec.terminate()
        try:
            surec.wait(timeout=20)
        except subprocess.TimeoutExpired:
            surec.kill()


if __name__ == "__main__":
    main()
