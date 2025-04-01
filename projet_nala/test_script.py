from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from faker import Faker
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Générer des données fictives
fake = Faker()

# Configuration du driver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Ouvrir l'application R Shiny
url = "https://nubho7-ruben-kouame.shinyapps.io/test_Projet_nalan/"
driver.get(url)
time.sleep(5)  # Attendre le chargement de la page

for _ in range(2):  # Remplir 50 formulaires
    # Remplir les champs avec les bons ID
    # Attendre que le champ "name" soit cliquable
    name_field = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "name"))
)
    driver.find_element(By.ID, "name").send_keys(fake.name())
    driver.find_element(By.ID, "email").send_keys(fake.email())

    driver.find_element(By.ID, "numero").send_keys(fake.phone_number())

    from selenium.webdriver.support.ui import Select

    from selenium.webdriver.common.keys import Keys

   
    # Attendre que l'élément soit réactualisé et interactif
    pays_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pays-selectized"))
    )
    driver.find_element(By.ID, "pays-selectized").send_keys("Côte d'Ivoire")


    #pays_input.send_keys("Côte d'Ivoire")  # Taper le pays
    time.sleep(2)  # Attendre que la liste apparaisse
   
    # Attendre que l'élément soit réactualisé et interactif
    ville_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ville-selectized"))
    )
    driver.find_element(By.ID, "ville-selectized").send_keys("Abidjan")
    #ville_input.send_keys("Abidjan")
    time.sleep(2)
    
    driver.find_element(By.ID, "quartier").send_keys(fake.city())
    driver.find_element(By.ID, "adresse_livraison").send_keys(fake.address())
    driver.find_element(By.ID, "preferences").send_keys("Aucune préférence")

    # Cliquer sur le bouton "Enregistrer"
    driver.find_element(By.ID, "submit").click()
    
    time.sleep(2)  # Attendre que les données s'affichent avant le prochain remplissagey

print("5 formulaires remplis avec succès !")
driver.quit()
"""
from faker import Faker
fake = Faker()
print(fake.name())  # Vérifie si ça fonctionne'
"""
