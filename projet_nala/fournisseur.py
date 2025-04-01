
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
    driver.find_element(By.ID, "fournisseur_nom").send_keys(fake.name())
    driver.find_element(By.ID, "fournisseur_email").send_keys(fake.email())

    driver.find_element(By.ID, "fournisseur_telephone").send_keys(fake.phone_number())

    from selenium.webdriver.support.ui import Select

    from selenium.webdriver.common.keys import Keys

   
    # Attendre que l'élément soit réactualisé et interactif
   
    driver.execute_script("document.getElementById('fournisseur_pays').value = 'Côte d\\'Ivoire';")
    driver.execute_script("document.getElementById('fournisseur_pays').dispatchEvent(new Event('change'));")

    driver.execute_script("document.getElementById('fournisseur_type').value = 'Abidjan';")
    driver.execute_script("document.getElementById('fournisseur_type').dispatchEvent(new Event('change'));")

    
    driver.find_element(By.ID, "fournisseur_livraison").send_keys(fake.address())

    driver.find_element(By.ID, "fournisseur_site").send_keys(fake.city())

    driver.find_element(By.ID, "fournisseur_responsable").send_keys(fake.name())
    driver.find_element(By.ID, "fournisseur_contact").send_keys(fake.name())

    # Cliquer sur le bouton "Enregistrer"
    driver.find_element(By.ID, "submit").click()
    
    time.sleep(2)  # Attendre que les données s'affichent avant le prochain remplissagey

print(" formulaires remplis avec succès !")
driver.quit()

