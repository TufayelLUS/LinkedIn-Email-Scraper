from linkedin import LinkedIn
email = "someone@example.com" #set username
password = "example_password" #set password
target_profile = "https://www.linkedin.com/in/tufayel-ahmed-cse/" #set target profile url
client = LinkedIn()
if client.login(email, password):
    
    #for single profile
    print(client.singleScan(target_profile))
    
    #for bulk list
    #profiles = ["PROFILE_URL_1","PROFILE_URL_2"]
    #print(client.bulkScan(target_profile))
else:
    print("Login Failed, please recheck login credentials")
