#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:00:09 2021

@author: emilejetzer
"""


from pathlib import Path
from datetime import datetime as Dt
import io
from xml.etree.ElementTree import parse, fromstring

#from markdownify import markdownify as mdc
import html2markdown
import PyRSS2Gen as rss
import markdown as md
from bs4 import BeautifulSoup
import unidecode
import os
# Constantes, à envoyer dans un fichier de configuration à terme
FLUX = Path.cwd() / 'electron_libre.rss'

GLOB = '*.html'
AUTEUR = '"PHYSUM-Électron libre" <  electron.libre.physum@outlook.com>'


def nouveau_flux(title: str, link: str, description: str) -> parse:
    """
    Crée un nouveau flux RSS.

    Parameters
    ----------
    title : str
        Titre du flux RSS.
    link : str
        Lien vers le flux RSS.
    description : str
        Description générale du contenu.

    Returns
    -------
    parse
        Arbre XML (ElementTree).

    """
    flux = rss.RSS2(title, link, description, pubDate=Dt.now())

    # rss.RSS2.write_xml ne retourne pas de valeur, il fait juste écrire dans
    # un fichier ou similaire
    f = io.StringIO()
    flux.write_xml(f)
    f.seek(0)

    return parse(f)  # Retourner un arbre XML


def nouvel_item(title: str, link: str, description: str, author: str,
                pubDate: Dt) -> parse:
    """
    Crée un nouvel item (article) dans un flux RSS.

    Parameters
    ----------
    title : str
        Titre de l'item.
    link : str
        Lien vers l'item.
    description : str
        Contenu de l'article.
    author : str
        Nom et courriel de l'auteur.
    pubDate : Dt
        Date de publication.

    Returns
    -------
    parse
        Arbre XML (ElementTree).

    """
    item = rss.RSSItem(title=title,
                       link=link,
                       description=description,
                       author=author,
                       pubDate=pubDate,
                       guid=rss.Guid(link))  # id unique dans le canal

    # rss.RSS2.write_xml ne retourne pas de valeur, il fait juste écrire dans
    # un fichier ou similaire
    f = io.StringIO()
    item.write_xml(f)
    f.seek(0)

    return parse(f)


def charger_article(f: Path,subfolder) -> (str, str, str, str, Dt,str):
    """
    Charge un fichier markdown comme article.

    Parameters
    ----------
    f : Path
        Chemin de l'article à charger.

    Returns
    -------
    (str, str, str, str, Dt)
        Arguments pour la fonction nouvel_item.

    """
    global_link="https://l-electron-libre.github.io/texte/"+subfolder

    pubDate = Dt.fromtimestamp(f.stat().st_ctime)


    with f.open(encoding='utf-8') as d:
        soup = BeautifulSoup(d.read(),features="html.parser")

        soup2 = soup.find("section", {"id": "One"})
        soup2 = soup2.findChildren(recursive=False)[0]
        title = soup2.find("h2")
        title = unidecode.unidecode(title.get_text())
        link =global_link+"/"+f.name

        soup = soup.find("section", {"id": "two"})
        soup = soup.findChildren(recursive=False)[0]
        title2=soup.find("h2")
        title2 = unidecode.unidecode(title2.get_text())
        title = title + " - " +html2markdown.convert(title2)





        author = soup.find("h3")
        if author is None :
            author=""
        else :
            author=html2markdown.convert(author.get_text())

        description = soup.find("p")
        description = unidecode.unidecode(description.get_text())

        description =  html2markdown.convert(description)

    # L'ordre est important, voir nouvel_item
    return title, link, author, description,pubDate


def main():
    """Script de démo."""
    flux = parse(FLUX) if FLUX.exists()\
        else nouveau_flux('Test', 'www.com', '...')
    canal = flux.find('./channel')

    if canal.find('./lastBuildDate') is None:
        canal.insert(0,
                     fromstring(
                         f'<lastBuildDate>{Dt.utcnow()}</lastBuildDate>'))
    else:
        canal.find('./lastBuildDate').text = str(Dt.utcnow())
    articles = [a.text for a in canal.findall('./item/guid')]
    for x in FLUX.parent.iterdir() :
        for a in x.glob(GLOB):
            article = charger_article(a,x.name)
            if article[1] not in articles:
                item = nouvel_item(*article)
                canal.append(item.getroot())

    flux.write(FLUX, encoding='utf-8', xml_declaration=True)


if __name__ == '__main__':
    main()
