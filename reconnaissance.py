from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image =image.binarisation(S)
    image = image.localisation()
    sim = 0
    chiffre = 0
    for i in range (len(liste_modeles)):
        image2 = liste_modeles[i]
        image = image.resize(image2.H, image.W)
        im = image.similitude(image2)
        if im > sim:
            sim = im
            chiffre = 1
    return chiffre

