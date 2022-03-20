"""
dev: Costea Adrian
scope: A program that automatically uploades files to helios for the software engineering lab
"""
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#login to helios
def login(drive, user_name, password):
    #go to helios
    driver.get('https://helios.utcluj.ro/LEARN2CODE/login.php?SID')
    #wait a litl bit for it to load
    time.sleep(1)

    #enter username
    userBox = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[1]/td[2]/input')
    userBox.send_keys(user_name)
    time.sleep(1)

    #enter password
    passwordBox = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[2]/td[2]/input')
    passwordBox.send_keys(password)
    time.sleep(1)

    #click login button
    loginButton = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[4]/td/button')
    loginButton.click()
    time.sleep(1)

#go to work area
def go_to_work_area(driver):
    #click the work area button
    workAreBtn = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[2]/div[1]/div/div[4]')
    workAreBtn.click()
    time.sleep(1)

#create addNewFileBtn address
def create_add_new_file_btn_address(labName):
    addNewFileAddress = '/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td/table/tbody/tr[' + str(labName+1) + ']/td[3]/a'
    return addNewFileAddress

#upload file
def add_new_file(driver, filePath, labName):

    #generate add new file button address
    addNewFileBtnAddress = create_add_new_file_btn_address(labName)
    print(addNewFileBtnAddress)

    #click the add new file button
    addFileBtn = driver.find_element(by=By.XPATH, value=addNewFileBtnAddress)
    addFileBtn.click()
    time.sleep(1)

    #click the chose file button
    choseFileBtn = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[5]/td[2]/input[1]')
    choseFileBtn.send_keys(filePath)
    time.sleep(1)

    #click the save file button
    saveFileBtn = driver.find_element(by=By.XPATH, value='/html/body/div/div[2]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/table/tbody/tr[7]/td/button')
    saveFileBtn.click()
    time.sleep(1)


#add all of the files to your lab
#add all of the files to your lab
def add_all_files(driver, pathToLabFiles, labName):
    inputs = []
    # luam fisierele care se termina cu .txt si le salvam in inputs
    for file in os.listdir(pathToLabFiles):
        if file.endswith(".txt"):
            inputs.append(os.path.join(pathToLabFiles, file))

    #parcurgem fisierele din folder si le adaugam pe helios
    for fname in inputs:
        print(fname)
        add_new_file(driver, fname, labName)
if __name__ == '__main__':

    #get user credits and data about the lab
    print("Add lab to Helios automatically\n")
    print("User_Name: ")
    user_name = input()
    print("Password: ")
    password = input()
    print("Path de la folderul cu problemele: ")
    folderPath = input()
    print("Laboratorul de la care sunt problemele (doar un numar intreg): ")
    labName = input()
    labName = int(labName)

    #start the selenium and upload files
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    login(driver, user_name, password)
    go_to_work_area(driver)

    #add_new_file(driver, r'C:\Users\adivd\OneDrive\Desktop\Lab4\Costea Adrian_G1_An2_Lab4_Ex1.txt')
    add_all_files(driver, folderPath, labName)

    #close the Chrome Window
    driver.close()

    #print the succesfull message
    print("Files uploaded successfully")


