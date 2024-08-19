import socket
import re
import time
import codecs

# Paramètres de connexion
host = "challenge01.root-me.org"
port = 52021

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
            if "my string is" in line:
                print("Ligne à traiter :", line)
                
                
               
                # Extraction de la chaîne entre les guillemets simples
                match = re.search(r"'(.*?)'", line)
                
                if match:
                    extracted_string = match.group(1)
                    print("Chaîne extraite :", extracted_string)
                    decode = codecs.decode(extracted_string, 'rot_13')
                    print("Chaîne décodée :", decode)
                    
                    # Envoyer la réponse au serveur avec un retour à la ligne
                s.sendall((str(decode) + '\n').encode())
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
