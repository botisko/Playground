"""Daily Menus of restaurants near Honeywell Brno"""

"""lxml package is requied"""

import sys

from lxml import html
import requests

webs = ['http://www.restaurant-goa-slatina.cz/lang-cs/denni-menu', 'https://www.alltasty.cz', 'http://honeywell-brno-2.portal.sodexo.cz/cs/jidelni-listek-na-cely-tyden']
trees = ['//div[@class="floatbox"]//td[@valign="top"]//text()', '//div[@class="left-div item-name"]//text()', '//div[@id="menu-4"]//div[@class="content"]//table[@class="food"]//td[@class="popisJidla"]/text()']

def getMenu(sel):
    """Get menus from selected restaurants"""
    page = requests.get(webs[sel])
    tree = html.fromstring(page.content)

    selMenu = tree.xpath(trees[sel])

    return selMenu

def printMenu(numMenu, selMenu):
    """Print the wanted menu"""
    if numMenu == 1:
    # GOA
        print(selMenu[8])
        print(selMenu[10:-33])
    elif numMenu == 2:
    # AllTasty
        #print(selMenu[:])
        print('This restaurant is not implemented yet.')
    # Sodexo
    elif numMenu == 3:
        print(selMenu[:])
    else:
        print("Wrong restaurant...")

def main():
    """Main script menu"""
    sel = input("Please select desired restaurant:\n\t1) GOA\n\t2) AllTasty\n\t3) Sodexo\n\t4) All of the above\n ")
    selMenu = getMenu(int(sel)-1)
    # vyjimka - check numerka
    # neco jsem zadal?
    printMenu(int(sel), selMenu)

if __name__ == '__main__':
    main()
