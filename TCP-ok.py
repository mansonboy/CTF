import socket
import math
import re
import time

# Paramètres de connexion
host = "challenge01.root-me.org"
port = 52002

def main():
    start_time = time.time()
    
    # Création d'une socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Connexion au serveur
        s.connect((host, port))
        
        # Lecture des données envoyées par le serveur
        data = s.recv(1024).decode()
        print("Données reçues :", data)
        
        # Rechercher la ligne contenant l'opération mathématique
        for line in data.splitlines():
            if "Calculate the square root of" in line:
                print("Ligne à traiter :", line)
                
                # Extraction des nombres à l'aide d'une expression régulière
                numbers = re.findall(r'\d+', line)
                n1 = float(numbers[0])  # Le premier nombre est n°1 (racine carrée)
                n2 = float(numbers[1])  # Le second nombre est n°2 (multiplication)
                
                print(f"n1 = {n1}, n2 = {n2}")
                
                # Calcul de la racine carrée de n°1, puis multiplication par n°2
                result = math.sqrt(n1) * n2
                
                # Arrondir à deux chiffres après la virgule
                result = round(result, 2)
                
                print(f"Résultat calculé : {result}")
                
                # Envoyer la réponse au serveur avec un retour à la ligne
                s.sendall((str(result) + '\n').encode())
                print("Résultat envoyé au serveur.")
                
                # Lire la réponse du serveur
                response = s.recv(1024).decode()
                print("Réponse du serveur :", response)
                break
        
        # Vérifier si le délai est respecté
        elapsed_time = time.time() - start_time
        print(f"Temps écoulé : {elapsed_time:.4f} secondes")
        if elapsed_time > 2:
            print("Attention : Le délai de 2 secondes a été dépassé.")

if __name__ == "__main__":
    main()
