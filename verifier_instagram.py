import instaloader
from colorama import Fore, init

# Initialisation de colorama pour la couleur dans le terminal
init(autoreset=True)

# Affichage du logo avec couleurs
logo = f"""
{Fore.RED}        .                                                      .
{Fore.YELLOW}        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
{Fore.GREEN} 4    qXb         .       dX                     Xb       .        dXp     t
{Fore.CYAN}dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
{Fore.MAGENTA}9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
{Fore.BLUE} 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
{Fore.YELLOW}  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'  ByKLN   `98v8P' GANG `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
          {Fore.RED}FUCK        dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb        BY
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
          OPS                  XXXX X.`v'.X XXXX                 KLN
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `  <2    '  d'
"""

# Affichage du logo
print(logo)

# Fonction pour récupérer les informations publiques du compte Instagram
def get_instagram_info(username):
    L = instaloader.Instaloader()

    try:
        # Charger le profil utilisateur sans login ni cookies
        profile = instaloader.Profile.from_username(L.context, username)

        # Récupérer les informations du profil
        info = {
            "username": profile.username,
            "full_name": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "followees": profile.followees,
            "is_verified": profile.is_verified,
            "profile_pic_url": profile.get_profile_pic_url()
        }

        return info

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Fore.RED}Le profil {username} n'existe pas.")
        return None
    except Exception as e:
        print(f"{Fore.RED}Une erreur est survenue : {Fore.WHITE}{e}")
        return None

# Fonction pour afficher les détails d'un utilisateur
def display_profile_info(profile_info):
    if profile_info is None:
        print(f"{Fore.RED}Aucune information à afficher.")
        return

    print(f"\n{Fore.GREEN}Informations pour l'utilisateur {profile_info['username']} :\n")
    print(f"Nom complet : {Fore.WHITE}{profile_info['full_name']}")
    print(f"Bio : {Fore.WHITE}{profile_info['bio']}")
    print(f"Nombre d'abonnés : {Fore.WHITE}{profile_info['followers']}")
    print(f"Nombre de suivis : {Fore.WHITE}{profile_info['followees']}")
    print(f"Utilisateur certifié : {Fore.WHITE}{'Oui' if profile_info['is_verified'] else 'Non'}")
    print(f"Photo de profil URL : {Fore.WHITE}{profile_info['profile_pic_url']}")

# Fonction pour afficher les crédits et les réseaux sociaux
def show_credits():
    print(f"\n{Fore.CYAN}Crédits & Réseaux Sociaux :\n")
    print(f"{Fore.YELLOW}Instagram: {Fore.WHITE}@kln.213_")
    print(f"{Fore.BLUE}Discord: {Fore.WHITE}@bykln")
    print(f"{Fore.GREEN}DeepCord: {Fore.WHITE}https://discord.gg/zw97FqBQk8")
    print(f"{Fore.RED}GitHub: {Fore.WHITE}https://github.com/ByKLN667")
    print(f"{Fore.MAGENTA}Merci d'utiliser InstaK !")

if __name__ == "__main__":
    while True:
        print(f"{Fore.CYAN}Choisissez une option :")
        print(f"1. Voir les informations d'un utilisateur")
        print(f"2. Comparer deux utilisateurs")
        print(f"3. Voir les crédits et réseaux sociaux")
        print(f"4. Quitter")

        choice = input(f"{Fore.YELLOW}Votre choix : {Fore.WHITE}")

        if choice == "1":
            username = input(f"{Fore.RED}Entrez le nom d'utilisateur Instagram : {Fore.WHITE}")
            profile_info = get_instagram_info(username)
            display_profile_info(profile_info)

        elif choice == "2":
            username1 = input(f"{Fore.RED}Entrez le premier nom d'utilisateur Instagram : {Fore.WHITE}")
            username2 = input(f"{Fore.RED}Entrez le second nom d'utilisateur Instagram : {Fore.WHITE}")

            profile1_info = get_instagram_info(username1)
            profile2_info = get_instagram_info(username2)

            # Comparaison entre les profils
            if profile1_info and profile2_info:
                print(f"\nComparaison entre {profile1_info['username']} et {profile2_info['username']} :\n")
                print(f"{profile1_info['username']} - Abonnés : {profile1_info['followers']}")
                print(f"{profile2_info['username']} - Abonnés : {profile2_info['followers']}")
                
                if profile1_info['followers'] > profile2_info['followers']:
                    print(f"{profile1_info['username']} a plus d'abonnés.")
                elif profile1_info['followers'] < profile2_info['followers']:
                    print(f"{profile2_info['username']} a plus d'abonnés.")
                else:
                    print("Les deux utilisateurs ont le même nombre d'abonnés.")

        elif choice == "3":
            show_credits()  # Affiche les crédits et les réseaux sociaux

        elif choice == "4":
            print(f"{Fore.GREEN}Au revoir !")
            break

        else:
            print(f"{Fore.RED}Choix invalide. Veuillez réessayer.")
