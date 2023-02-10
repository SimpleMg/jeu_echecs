import numpy as np


class VerifyCoup:
    def __init__(self, pseudo):
        self.pseudo = pseudo

    def _recupere_indice(self, choice_pion, grille):
        indice = []
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if choice_pion == grille[i][j]:
                    indice = [i, j]
        return indice

    def _recup_element(self, grille, choice_user):
        sump = 0
        for i in range(len(grille)):
            for j in range(len(grille[i])):
                if (8 * i) + j == choice_user:
                    sump = grille[i][j]
        return sump

    def _def_deplacement_pion(self, choice_user, mouvement_pion, grille, choix_pion):
        sump = self._recup_element(grille, choice_user)
        test_pos = abs((list(zip(*np.where(grille == choix_pion)))
                       [0][0]) - (list(zip(*np.where(grille == str(sump))))[0][0]))
        if mouvement_pion[choix_pion] == 0 and test_pos == 2:
            deplacement = 2
            mouvement_pion[choix_pion] += 2  
        elif mouvement_pion[choix_pion] >= 1 and test_pos >= 2:
            print("mauvais déplacement vous avez le droit d'avancer que une fois\n")
            deplacement = -1
        elif test_pos < 2:
            deplacement = 1
            mouvement_pion[choix_pion] += 1  
        else:
            deplacement = -1
        return deplacement

    def _verify_depla_pion(self, choice_user, grille, choix_pion, mouvement_pion, pion_manger, player_pseudo, pion_user):
        deplacement = self._def_deplacement_pion(
            choice_user, mouvement_pion, grille, choix_pion)
        indice = self._recupere_indice(choix_pion, grille)
        sump = self._recup_element(grille, choice_user)
        indice_choice_user = self._recupere_indice(str(sump), grille)
        if deplacement == 2:
            stock = 0
            try:
                if choix_pion.startswith("PB"):
                    if int(grille[indice[0]+1][indice[1]]) and int(grille[indice[0]+2][indice[1]]):
                        stock = (indice[0] * 8) + indice[1]
                        grille[indice[0]+2][indice[1]
                                            ] = grille[indice[0]][indice[1]]
                        grille[indice[0]][indice[1]] = stock
                        return indice
                else:
                    if int(grille[indice[0]-1][indice[1]]) and int(grille[indice[0]-2][indice[1]]):
                        stock = (indice[0] * 8) + indice[1]
                        grille[indice[0]-2][indice[1]
                                            ] = grille[indice[0]][indice[1]]
                        grille[indice[0]][indice[1]] = stock
                        return indice

            except:
                print("déja un pion droit devant")
        elif deplacement == 1:
            try:
                if choix_pion.startswith("PB"):
                    try:
                        grille[indice_choice_user[0]][indice_choice_user[1]
                                                      ] = int(grille[indice_choice_user[0]][indice_choice_user[1]])
                        if choice_user == int(grille[indice[0]+1][indice[1]]):
                            stock = (indice[0] * 8) + indice[1]
                            grille[indice_choice_user[0]][indice_choice_user[1]
                                                          ] = grille[indice[0]][indice[1]]
                            grille[indice[0]][indice[1]] = (stock)
                            return indice
                    except:
                        if str(sump) not in pion_user:
                            indice_pion_manger_droite = self._recupere_indice(
                                str(grille[indice[0]+1][indice[1]+1]), grille)
                            indice_pion_manger_gauche = self._recupere_indice(
                                str(grille[indice[0]+1][indice[1]-1]), grille)
                            if sump == grille[indice_pion_manger_droite[0]][indice_pion_manger_droite[1]]:
                                stock = (indice[0] * 8) + indice[1]
                                pion_manger[player_pseudo].append(str(
                                    grille[indice[0]+1][indice[1]+1]))
                                grille[indice[0]+1][indice[1] + 1
                                                    ] = choix_pion
                                grille[indice[0]][indice[1]] = stock
                                return pion_manger
                            elif sump == grille[indice_pion_manger_gauche[0]][indice_pion_manger_gauche[1]]:
                                stock = (indice[0] * 8) + indice[1]
                                pion_manger[player_pseudo].append(str(
                                    grille[indice[0]+1][indice[1]-1]))
                                grille[indice[0]+1][indice[1] - 1
                                                    ] = choix_pion
                                grille[indice[0]][indice[1]] = stock
                                return pion_manger
                            else:
                                return -1
                        else:
                            print("on ne peut manger un pion allié\n")
                            return -1
                else:
                    try:
                        grille[indice_choice_user[0]][indice_choice_user[1]
                                                      ] = int(grille[indice_choice_user[0]][indice_choice_user[1]])
                        if choice_user == int(grille[indice[0]-1][indice[1]]):
                            stock = (indice[0] * 8) + indice[1]
                            grille[indice_choice_user[0]][indice_choice_user[1]
                                                          ] = grille[indice[0]][indice[1]]
                            grille[indice[0]][indice[1]] = stock
                            return pion_manger
                    except:
                        if str(sump) not in pion_user:
                            indice_pion_manger_droite = self._recupere_indice(
                                str(grille[indice[0]-1][indice[1]+1]), grille)
                            indice_pion_manger_gauche = self._recupere_indice(
                                str(grille[indice[0]-1][indice[1]-1]), grille)
                            sump = self._recup_element(grille, choice_user)
                            if sump == grille[indice_pion_manger_droite[0]][indice_pion_manger_droite[1]]:
                                stock = (indice[0] * 8) + indice[1]
                                pion_manger[player_pseudo].append(str(
                                    grille[indice[0]-1][indice[1]+1]))
                                grille[indice[0]-1][indice[1] + 1
                                                    ] = choix_pion
                                grille[indice[0]][indice[1]] = stock
                                return pion_manger
                            elif sump == grille[indice_pion_manger_gauche[0]][indice_pion_manger_gauche[1]]:
                                stock = (indice[0] * 8) + indice[1]
                                pion_manger[player_pseudo].append(str(
                                    grille[indice[0]-1][indice[1]-1]))
                                grille[indice[0]-1][indice[1] - 1
                                                    ] = choix_pion
                                grille[indice[0]][indice[1]] = stock
                                return pion_manger
                            else:
                                return -1
                        else:
                            print("on ne peut manger un pion allié\n")
                            return -1
            except:
                print("mauvais deplacement")
                return -1
        else:
            print("mauvais deplacement")
            return -1

    def _verify_depla_cavalier(
            self, choice_user, grille, choix_pion, pion_manger, player_pseudo, pion_user):
        sump = self._recup_element(grille, choice_user)
        indice = self._recupere_indice(choix_pion, grille)
        indice_choice_user = self._recupere_indice(str(sump), grille)
        if (indice[0]+2) == indice_choice_user[0] and (indice[1]-1) == indice_choice_user[1]:
            stock = (indice[0] * 8) + indice[1]
            try:
                grille[indice[0]+2][indice[1] -
                                    1] = int(grille[indice[0]+2][indice[1]-1])
            except:
                if str(sump) not in pion_user:
                    pion_manger[player_pseudo].append(
                        str(grille[indice[0]+2][indice[1]-1]))
                else:
                    print("on ne peut manger un pion allié\n")
                    return -1
            grille[indice[0]+2][indice[1]-1] = grille[indice[0]][indice[1]]
            grille[indice[0]][indice[1]] = stock
            return pion_manger
        elif (indice[0]-2) == indice_choice_user[0] and (indice[1]+1) == indice_choice_user[1]:
            stock = (indice[0] * 8) + indice[1]
            try:
                grille[indice[0]-2][indice[1] +
                                    1] = int(grille[indice[0]-2][indice[1]+1])
            except:
                if str(sump) not in pion_user:
                    pion_manger[player_pseudo].append(
                        str(grille[indice[0]-2][indice[1]+1]))
                else:
                    print("on ne peut manger un pion allié\n")
                    return -1
            grille[indice[0]-2][indice[1]+1] = grille[indice[0]][indice[1]]
            grille[indice[0]][indice[1]] = stock
            return pion_manger
        elif (indice[0]+2) == indice_choice_user[0] and (indice[1]+1) == indice_choice_user[1]:
            stock = (indice[0] * 8) + indice[1]
            try:
                grille[indice[0]+2][indice[1] +
                                    1] = int(grille[indice[0]+2][indice[1]+1])
            except:
                if str(sump) not in pion_user:
                    pion_manger[player_pseudo].append(
                        str(grille[indice[0]+2][indice[1]+1]))
                else:
                    print("on ne peut manger un pion allié\n")
                    return -1
            grille[indice[0]+2][indice[1]+1] = grille[indice[0]][indice[1]]
            grille[indice[0]][indice[1]] = stock
            return pion_manger
        elif (indice[0]-2) == indice_choice_user[0] and (indice[1]-1) == indice_choice_user[1]:
            stock = (indice[0] * 8) + indice[1]
            try:
                grille[indice[0]-2][indice[1] -
                                    1] = int(grille[indice[0]-2][indice[1]-1])
            except:
                if str(sump) not in pion_user:
                    pion_manger[player_pseudo].append(
                        str(grille[indice[0]-2][indice[1]-1]))
                else:
                    print("on ne peut manger un pion allié\n")
                    return -1
            grille[indice[0]-2][indice[1]-1] = grille[indice[0]][indice[1]]
            grille[indice[0]][indice[1]] = stock
            return pion_manger
        else:
            print("mauvais deplacement\n")
            return -1
    

    def _verify_depla_tour(self, choice_user, grille,
                           choix_pion, pion_manger, player_pseudo, pion_user):
        sump = self._recup_element(grille, choice_user)
        indice = self._recupere_indice(choix_pion, grille)
        indice_choice_user = self._recupere_indice(str(sump), grille)
        if indice_choice_user[0] != indice[0] and indice_choice_user[1] != indice[1]:
            print("mauvais déplacement\n")
            return -1  # deplacement non perpendicaulaire
        else:
            stock = (8 * indice[0]) + (indice[1])
            try:
                if indice[0] != indice_choice_user[0]:
                    if indice[0] > indice_choice_user[0]:
                        for i in range(indice[0] - 1, indice_choice_user[0], -1):
                            if str(grille[i][indice_choice_user[1]]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                    else:
                        for i in range(indice[0] + 1, indice_choice_user[0]):
                            if str(grille[i][indice_choice_user[1]]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                else:
                    if indice[1] > indice_choice_user[1]:
                        for i in range(indice[1]-1, indice_choice_user[1], -1):
                            if str(grille[indice_choice_user[0]][i]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                    else:
                        for i in range(indice[1] + 1, indice_choice_user[1]):
                            if str(grille[indice_choice_user[0]][i]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = int(grille[indice_choice_user[0]][indice_choice_user[1]])
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = str(grille[indice[0]][indice[1]])

                grille[indice[0]][indice[1]] = stock

                return pion_manger
            except:
                if str(sump) not in pion_user:
                    pion_manger[player_pseudo].append(
                        str(grille[indice_choice_user[0]][indice_choice_user[1]]))
                    grille[indice_choice_user[0]][indice_choice_user[1]
                                                  ] = str(grille[indice[0]][indice[1]])
                else:
                    print("on ne peut manger un pion allié\n")
                    return -1
                grille[indice[0]][indice[1]] = stock
                return pion_manger

    def _verify_depla_fou(self, choice_user, grille,
                          choix_pion, pion_manger, player_pseudo, pion_user):
        sump = self._recup_element(grille, choice_user)
        indice = self._recupere_indice(choix_pion, grille)
        indice_choice_user = self._recupere_indice(str(sump), grille)
        compteur_diagonale_i = indice_choice_user[0]
        compteur_diagonale_j = indice_choice_user[1]
        if indice[0] < indice_choice_user[0]:  # sens inverse
            if indice_choice_user[1] < indice[1]:
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                        print("on ne peut manger un pion allié\n")
                        return -1
                    compteur_diagonale_i -= 1
                    compteur_diagonale_j += 1

            elif indice_choice_user[1] > indice[1]:
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                        print("on ne peut manger un pion allié\n")
                        return -1
                    compteur_diagonale_i -= 1
                    compteur_diagonale_j -= 1

        else:  # sens normal
            if indice[1] < indice_choice_user[1]:
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                        print("on ne peut manger un pion allié\n")
                        return -1
                    compteur_diagonale_i += 1
                    compteur_diagonale_j -= 1
            elif indice[1] > indice_choice_user[1]:
                if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                    print("on ne peut manger un pion allié\n")
                    return -1
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    compteur_diagonale_i += 1
                    compteur_diagonale_j += 1
        if str(grille[compteur_diagonale_i][compteur_diagonale_j]) != str(choix_pion):
            return -1
        else:
            stock = (8 * indice[0]) + (indice[1])
            try:
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = int(grille[indice_choice_user[0]][indice_choice_user[1]])
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = str(grille[indice[0]][indice[1]])
                grille[indice[0]][indice[1]] = stock
                return pion_manger
            except:
                pion_manger[player_pseudo].append(
                    str(grille[indice_choice_user[0]][indice_choice_user[1]]))
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = str(grille[indice[0]][indice[1]])
                grille[indice[0]][indice[1]] = stock
                return pion_manger  # diagonale (donc avance)

    def _verify_depla_dame(self, choice_user, grille,
                           choix_pion, pion_manger, player_pseudo, pion_user):
        sump = self._recup_element(grille, choice_user)
        indice = self._recupere_indice(choix_pion, grille)
        indice_choice_user = self._recupere_indice(str(sump), grille)
        if abs(indice_choice_user[1] - indice[1]) in [0, 1] and abs(indice_choice_user[0] - indice[0]) in [0, 1]:
            stock = (8 * indice[0]) + (indice[1])
            try:
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = int(grille[indice_choice_user[0]][indice_choice_user[1]])
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = str(grille[indice[0]][indice[1]])
                grille[indice[0]][indice[1]] = stock
                return pion_manger
            except:
                if str(sump) not in pion_user:
                    pion_manger[player_pseudo].append(
                        str(grille[indice_choice_user[0]][indice_choice_user[1]]))
                    grille[indice_choice_user[0]][indice_choice_user[1]
                                                  ] = str(grille[indice[0]][indice[1]])
                else:
                    print("on ne peut manger un pion allié\n")
                    return -1
                grille[indice[0]][indice[1]] = stock
                return pion_manger
        else:
            print("mauvais deplacement")
            return -1

    def _verify_depla_roi(self, choice_user, grille,
                          choix_pion, pion_manger, player_pseudo, pion_user):
        sump = self._recup_element(grille, choice_user)
        indice = self._recupere_indice(choix_pion, grille)
        indice_choice_user = self._recupere_indice(str(sump), grille)
        mauv_deplaH = False
        mauv_deplaD = False
        # deplacement_horizontale
        if indice_choice_user[0] != indice[0] and indice_choice_user[1] != indice[1]:
            mauv_deplaH = False
        else:
            mauv_deplaH = True
            # deplacement en diagonale
        if mauv_deplaH:
            try:
                grille[indice_choice_user[0]][indice_choice_user[1]] = int(
                    grille[indice_choice_user[0]][indice_choice_user[1]])
                stock = (8 * indice[0]) + (indice[1])
                if indice[0] != indice_choice_user[0]:
                    if indice[0] > indice_choice_user[0]:
                        for i in range(indice[0] - 1, indice_choice_user[0], -1):
                            if str(grille[i][indice_choice_user[1]]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                    else:
                        for i in range(indice[0] + 1, indice_choice_user[0]):
                            if str(grille[i][indice_choice_user[1]]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                else:
                    if indice[1] > indice_choice_user[1]:
                        for i in range(indice[1]-1, indice_choice_user[1], -1):
                            if str(grille[indice_choice_user[0]][i]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                    else:
                        for i in range(indice[1] + 1, indice_choice_user[1]):
                            if str(grille[indice_choice_user[0]][i]) in pion_user:
                                print("on ne peut manger un pion allié\n")
                                return -1
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = str(grille[indice[0]][indice[1]])
                grille[indice[0]][indice[1]] = stock
                return pion_manger
            except:
                stock = (8 * indice[0]) + (indice[1])
                if str(sump) not in pion_user:
                    pion_manger[player_pseudo].append(
                        str(grille[indice_choice_user[0]][indice_choice_user[1]]))
                    grille[indice_choice_user[0]][indice_choice_user[1]
                                                  ] = str(grille[indice[0]][indice[1]])
                else:
                    print("on ne peut manger un pion allié\n")
                    return -1
                grille[indice[0]][indice[1]] = stock
                return pion_manger

        compteur_diagonale_i = indice_choice_user[0]
        compteur_diagonale_j = indice_choice_user[1]
        if indice[0] < indice_choice_user[0]:  # sens inverse
            if indice_choice_user[1] < indice[1]:
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                        print("on ne peut manger un pion allié\n")
                        return -1
                    compteur_diagonale_i -= 1
                    compteur_diagonale_j += 1
            elif indice_choice_user[1] > indice[1]:
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                        print("on ne peut manger un pion allié\n")
                        return -1
                    compteur_diagonale_i -= 1
                    compteur_diagonale_j -= 1
        else:  # sens normal
            if indice[1] < indice_choice_user[1]:
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                        print("on ne peut manger un pion allié\n")
                        return -1
                    compteur_diagonale_i += 1
                    compteur_diagonale_j -= 1
            elif indice[1] > indice_choice_user[1]:
                while grille[compteur_diagonale_i][compteur_diagonale_j] != grille[indice[0]][indice[1]]:
                    if str(grille[compteur_diagonale_i][compteur_diagonale_j]) in pion_user:
                        print("on ne peut manger un pion allié\n")
                        return -1
                    compteur_diagonale_i += 1
                    compteur_diagonale_j += 1
        if str(grille[compteur_diagonale_i][compteur_diagonale_j]) != str(choix_pion):
            mauv_deplaD = False
        else:
            mauv_deplaD = True
        if mauv_deplaD:
            try:
                grille[indice_choice_user[0]][indice_choice_user[1]] = int(
                    grille[indice_choice_user[0]][indice_choice_user[1]])
                stock = (8 * indice[0]) + (indice[1])
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = str(grille[indice[0]][indice[1]])
                grille[indice[0]][indice[1]] = stock
                return pion_manger
            except:
                stock = (8 * indice[0]) + (indice[1])
                pion_manger[player_pseudo].append(
                    str(grille[indice_choice_user[0]][indice_choice_user[1]]))
                grille[indice_choice_user[0]][indice_choice_user[1]
                                              ] = str(grille[indice[0]][indice[1]])
                grille[indice[0]][indice[1]] = stock
                return pion_manger  # diagonale (donc avance)

        return -1

    def _verify_coup(self, choice_user, choix_pion, grille, mouvement_pion, pion_manger, player_pseudo, pion_user):
        if choix_pion.startswith("P"):
            indice = self._verify_depla_pion(
                choice_user, grille, choix_pion, mouvement_pion, pion_manger, player_pseudo, pion_user)
            if indice == -1:
                return -1
            else:
                return indice
        elif choix_pion.startswith("C"):
            indice = self._verify_depla_cavalier(
                choice_user, grille, choix_pion, pion_manger, player_pseudo, pion_user)
            if indice == -1:
                return -1
            else:
                return indice
        elif choix_pion.startswith("T"):
            indice = self._verify_depla_tour(
                choice_user, grille, choix_pion, pion_manger, player_pseudo, pion_user)
            if indice == -1:
                return -1
            else:
                return indice
        elif choix_pion.startswith("F"):
            indice = self._verify_depla_fou(choice_user, grille,
                                            choix_pion, pion_manger, player_pseudo, pion_user)
            if indice == -1:
                return -1
            else:
                return indice
        elif choix_pion.startswith("D"):
            indice = self._verify_depla_dame(
                choice_user, grille, choix_pion, pion_manger, player_pseudo, pion_user)
            if indice == -1:
                return -1
            else:
                return indice
        elif choix_pion.startswith("R"):
            indice = self._verify_depla_roi(choice_user, grille,
                                            choix_pion, pion_manger, player_pseudo, pion_user)
            if indice == -1:
                return -1
            else:
                return indice
        else:
            return -1


class Player:
    def __init__(self, pseudo):
        self.pseudo = pseudo
        self.verify = VerifyCoup(pseudo)

    def _verify_int(self, choix_pion, grille, mouv_pion, pion_manger, player_pseudo, pion_user):
        choice_user = input("A qu'elle emplacement mettre votre pion: \n")
        try:
            choice_user = int(choice_user)
            indice = self.verify._verify_coup(
                choice_user, choix_pion, grille, mouv_pion, pion_manger, player_pseudo, pion_user)
            if indice == -1:
                print("pas un coup valide regardez bien les regles de déplacements")
                return self._verify_int(choix_pion, grille, mouv_pion, pion_manger, player_pseudo, pion_user)
            else:
                return indice
        except:
            print("merci de rentrez un entier\n")
            return self._verify_int(choix_pion, grille, mouv_pion, pion_manger, player_pseudo, pion_user)

    def choix_emplacement(self, pion, grille, mouv_pion, pion_manger, player_pseudo):
        choix_pion = ""
        while choix_pion not in pion:
            choix_pion = input(
                "que voulez vous jouer {} comme pion: {}".format(self.pseudo, pion))
        choix_emplacement = self._verify_int(
            choix_pion, grille, mouv_pion, pion_manger, player_pseudo, pion)
        return choix_emplacement


class MyGame:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.liste_player = [player_1, player_2]
        self.pion_manger = {player_1.pseudo: [], player_2.pseudo: []}
        self.score = {player_1.pseudo: [], player_2.pseudo: []}
        self.pion_blanc = {"PB1": "PB1", "PB2": "PB2", "PB3": "PB3", "PB4": "PB4", "PB5": "PB5",
                           "PB6": "PB6", "PB7": "PB7", "PB8": "PB8", "CB1": "CB1", "CB2": "CB2", "TB1": "TB1", "TB2": "TB2",
                           "FB1": "FB1", "FB2": "FB2", "DB1": "DB1", "RB1": "RB1"}

        self.pion_noir = {"PN1": "PN1", "PN2": "PN2", "PN3": "PN3", "PN4": "PN4", "PN5": "PN5",
                          "PN6": "PN6", "PN7": "PN7", "PN8": "PN8", "CN1": "CN1", "CN2": "CN2", "TN1": "TN1", "TN2": "TN2",
                          "FN1": "FN1", "FN2": "FN2", "DN1": "DN1", "RN1": "RN1"}

        self.mouvement_pion_count = {"PB1": 0, "PB2": 0, "PB3": 0, "PB4": 0, "PB5": 0,
                                     "PB6": 0, "PB7": 0, "PB8": 0,

                                     "PN1": 0, "PN2": 0, "PN3": 0, "PN4": 0, "PN5": 0,
                                     "PN6": 0, "PN7": 0, "PN8": 0
                                     }
        self.attribution_pion = {
            player_1.pseudo: self.pion_blanc, player_2.pseudo: self.pion_noir}
        self.grille = np.array([
            [self.pion_blanc["TB1"], self.pion_blanc["CB1"], self.pion_blanc["FB1"], self.pion_blanc["RB1"],
                self.pion_blanc["DB1"], self.pion_blanc["FB2"], self.pion_blanc["CB2"], self.pion_blanc["TB2"]],
            [self.pion_blanc["PB1"], self.pion_blanc["PB2"], self.pion_blanc["PB3"], self.pion_blanc["PB4"],
                self.pion_blanc["PB5"], self.pion_blanc["PB6"], self.pion_blanc["PB7"], self.pion_blanc["PB8"]],
            [i for i in range(16, 24)],
            [i for i in range(24, 32)],
            [i for i in range(32, 40)],
            [i for i in range(40, 48)],
            [self.pion_noir["PN1"], self.pion_noir["PN2"], self.pion_noir["PN3"], self.pion_noir["PN4"],
                self.pion_noir["PN5"], self.pion_noir["PN6"], self.pion_noir["PN7"], self.pion_noir["PN8"]],
            [self.pion_noir["TN1"], self.pion_noir["CN1"], self.pion_noir["FN1"], self.pion_noir["RN1"],
                self.pion_noir["DN1"], self.pion_noir["FN2"], self.pion_noir["CN2"], self.pion_noir["TN2"]],

        ])
        self._start_game()

    def _tour_joueur(self, tour_player):
        print("c'est au tour de {} de jouer".format(
            self.liste_player[tour_player].pseudo))
        return tour_player

    def _afficher_grille(self):
        print()
        print()
        if self.grille[0][0] == "0":
            print(self.grille[0][0], end="   ")
        for i in self.grille:
            for j in i:
                try:
                    if int(j):
                        print(j, end="   ")
                except:
                    print(j, end="  ")

            print()
        print()
        print()

    def _start_game(self):
        print("Bienvenue {} et {} voici la grille de jeux".format(
            self.player_1.pseudo, self.player_2.pseudo))
        self._afficher_grille()
        tour_player = 0
        gagnant = ""
        while True:
            if "DB1" in self.pion_manger[self.player_2.pseudo]:
                gagnant = self.player_2.pseudo
                break
            elif "DN1" in self.pion_manger[self.player_1.pseudo]:
                gagnant = self.player_1.pseudo
                break
            else:
                tour_player = self._tour_joueur(tour_player)
                if tour_player == 0:
                    play = self.player_1.choix_emplacement(
                        self.attribution_pion[self.player_1.pseudo], self.grille, self.mouvement_pion_count, self.pion_manger, self.player_1.pseudo)
                    if type(play) == dict:
                        self.pion_manger = play
                    print(self.pion_manger)
                    tour_player = 1
                else:
                    play = self.player_2.choix_emplacement(
                        self.attribution_pion[self.player_2.pseudo], self.grille, self.mouvement_pion_count, self.pion_manger, self.player_2.pseudo)
                    if type(play) == dict:
                        self.pion_manger = play
                    print(self.pion_manger)
                    tour_player = 0
                self._afficher_grille()
        if gagnant == self.player_1.pseudo:
            print("le gagnant est {}".format(self.player_1.pseudo))
        else:
            print("le gagnant est {}".format(self.player_2.pseudo))
