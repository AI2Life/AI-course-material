# imports
import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__() # change the cv2 limitation from 2^30 to 2^40
import cv2
import dlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import hashlib
import re


#%%

class Google_scraper:
    
    def __init__(self, max_images=100, 
                 color='original', 
                 resize_perc=250, 
                 faces_detector=False, 
                 hide_in_background=True):
        
        self.cwd = os.getcwd() # take the cwd       
        self.max_images = max_images # attribute: max number o pictures      
        self.color = color # attribute: color       
        self.resize_perc = resize_perc # attribute: resize percentage       
        self.faces_detector = faces_detector # attribute: face detector
        self.ff_detector = dlib.get_frontal_face_detector() # detector di facce       
        
        # time variables       
        self.sleeptime = 0.5
        self.scrolltime = 2.0        
        
        # clining variables        
        self.hwratio = 3.0 
        self.hash_list = list()
        
               
        # hide in background option
        
        self.hide_in_background = hide_in_background
        
        options = webdriver.ChromeOptions() # init chrome options
        options.add_argument('--headless') # set background option
        
        if not self.hide_in_background:
            self.driver = webdriver.Firefox(executable_path=os.path.join(self.cwd,
            "geckodriver")) # visible window
            
        else:
            self.driver = webdriver.Chrome(os.path.join(self.cwd,
            "chromedriver.exe"), options=options) # hidden window           
        
    

    # output method
    
    def search_and_download(self, search_list:list):
        
       
        self.search_list = search_list # list the searches
        
        for search in self.search_list:
            
            
            # SEARCH PICTURES
        
            self.create_dir(search) # method: create folder with the name of the search
            
            self.driver.get('https://www.google.it/imghp?hl=it') # get driver
            
            # accept cookies
            self.driver.find_element_by_xpath(
                '/html/body/div[2]/div[2]/div[3]/span/div/div/div[3]/button[2]').click()
            
            box = self.driver.find_element_by_xpath(
                '//*[@id="sbtc"]/div/div[2]/input') # google search box

            box.send_keys(search) # insert search in google search box
            box.send_keys(Keys.ENTER) # ENTER
            
            self.scroll() # method: scrolling the google page with all the results
            
            
            # DOWNLOAD PICTURES
            
            self.download_pictures(search) # method: download pictures
            
            
            # APPPLY COLOR/BW AND RESIZE
            
            self.face_dir = os.listdir(self.faces_path) # list downloaded pictures  
            
            for img in self.face_dir:
                
                if self.color == 'bw':
                    
                    self.cv_pic = cv2.imread(os.path.join(self.faces_path, 
                                                          img), cv2.IMREAD_GRAYSCALE) # read img (b/w)
                    print("resizing: " + img + "\n")
                    self.resize(img) # method: resize
                    
                elif self.color == 'original':
            
                    self.cv_pic = cv2.imread(os.path.join(self.faces_path, 
                                                          img)) # read img (original)
                    print("resizing: " + img + "\n")
                    self.resize(img) # method: resize picture
                                    
                # apply face dector
                              
                if self.faces_detector:
                    print("cropping faces from: " + img + "\n")
                    self.face_detector(img) # method: detect and crop face from picture 
                    

            # CLEANING
            
            self.face_dir = os.listdir(self.faces_path) # list edited pictures
            
            for img in self.face_dir:
                
                self.cv_pic = cv2.imread(os.path.join(self.faces_path, img)) # read picture
                                
                self.kill_bad_img(os.path.join(self.faces_path, img), 
                                  self.cv_pic) # method: delete pictures too small or with weird ratio
                
            
            # DELETE DUPLICATES    
       
            self.face_dir = os.listdir(self.faces_path) # list corrected pictures
           
            for img in self.face_dir:
                
                self.file_hash(os.path.join(self.faces_path, 
                                            img)) # method: take picture hash and put in a list
                

            for img, hashcode in zip(self.face_dir, self.hash_list):
                
                # if hash already present in hash_list, delete duplicate
                if self.hash_list.count(hashcode) > 1: # if hash is in list
                    os.remove(os.path.join(self.faces_path, img))
                    print(img + " is a duplicate: deleted! \n")

            self.hash_list = [] # empty hash_list
            
        
        # CLOSE DRIVER
       
        self.driver.close()
        
        
#%%       

    # inner methods

    def create_dir(self, directory:str):
        
        '''create folder with the name of the search'''
            
        self.directory = directory.replace(" ", "_") # put underscore in the folder name
        
        # create directory       
        self.faces_path = os.path.join(self.cwd, self.directory)  
        if not os.path.exists(self.faces_path):
                os.makedirs(self.faces_path)
    
   
    def scroll(self): 
        
        '''scrolling the google page with all the results'''
        
        self.last_height = self.driver.execute_script(
            'return document.body.scrollHeight') # obtain scroll height
        
        while True: # continue to scroll and look for "other results" button
            
            self.driver.execute_script(
                'window.scrollTo(0,document.body.scrollHeight)') # scroll
            
            time.sleep(self.scrolltime)
            new_height = self.driver.execute_script(
                'return document.body.scrollHeight') # obtain new height
            
            try:
                # click on "other results" if present
                self.driver.find_element_by_xpath(
                    '//*[@id="islmp"]/div/div/div/div/div[3]/div[2]/input').click()                
                time.sleep(self.scrolltime)
            except:
                pass
            
            if new_height == self.last_height:
                break
            
            self.last_height = new_height # update scroll height
        
        self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME) # return on top of the page
        time.sleep(self.scrolltime)    
        
                    
    def download_pictures(self, search:str):
        
        '''download pictures'''
    
        self.search = search
        
        self.driver.find_element_by_xpath(
            '//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img').click() # click on first image to obtain preview     
        time.sleep(self.sleeptime)
        
        # google preview
        self.img_to_screen = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img' 
        time.sleep(self.sleeptime)   
      
        self.driver.execute_script( # delete preview's cross
            """var l = document.getElementsByClassName("hm60ue")[0];l.parentNode.removeChild(l);""") 
        
        for i in range(1, self.max_images+1):
            
            right_arrow_butt = self.driver.find_element_by_xpath( # preview's right arrow
                '/html/body/div[2]/c-wiz/div[4]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[1]/a[3]')
            
            if right_arrow_butt.get_attribute("aria-disabled") == "true": # if preview's right arrows is not clickable
                print("last picture on page, closing... \n")
                break
                                  
            self.img_src = str(self.driver.find_element_by_xpath( # take the src (URL) of the image
                self.img_to_screen).get_attribute("src")) 
                
            self.img_src = re.sub(r'\W+', '', self.img_src) # delete symbols from picture src
            self.img_src = re.sub('_', '', self.img_src) # delete underscores to src
            self.img_src = self.img_src[-60:] # take last 60 character of src
            time.sleep(self.sleeptime)
            
            
            # delete other settings on preview
            self.driver.execute_script("""var l = document.getElementsByClassName("SIwKhe qMqo1b")[0];l.parentNode.removeChild(l);""") # remove google lens
            self.driver.execute_script("""var l = document.getElementsByClassName("SIwKhe D9XNA")[0];l.parentNode.removeChild(l);""") # remove sharing
            try:
                self.driver.execute_script("""var l = document.getElementsByClassName("AWxjD SIwKhe")[0];l.parentNode.removeChild(l);""") # remove clickable left arrow
            except:
                self.driver.execute_script("""var l = document.getElementsByClassName("AWxjD SIwKhe RDPZE")[0];l.parentNode.removeChild(l);""") # remove non-clickable left arrow
            self.driver.execute_script("""var l = document.getElementsByClassName("knIqbf SIwKhe")[0];l.parentNode.removeChild(l);""") # remove clicable right arrow


            time.sleep(self.sleeptime)  
            
            # define picture path
            self.file = os.path.join(self.cwd, self.search.replace(" ", "_"),
                                     str(i) + '_' + self.search.replace(" ", "_") + '_' + self.img_src +'.png')
            
            self.list_pictures = os.listdir(self.faces_path) # list pictures files
            
            # check if picture is already in the folder
            if any(self.img_src in path for path in self.list_pictures): # if there is any True return True
                print("This picture already exsits! Next! \n")
                time.sleep(self.sleeptime)    
                
                self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT) #  go to next picture
                time.sleep(self.sleeptime)
                
                continue
                
            else:
                
                print(str(i) + " saving: " + self.search.replace(" ", "_") + '_' 
                                          + self.img_src +'.png \n')
                
                # save screenshot of the picture
                self.driver.find_element_by_xpath(self.img_to_screen).screenshot(self.file)                  
                time.sleep(self.sleeptime) 
                
                self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT) # go to next picture
                time.sleep(self.sleeptime)


    def resize(self, pic:str):
        
        '''resize picture'''
   
        if "rs_" in pic:
            print("Picture already resized! Next! \n")
            pass

        else:
        
            try:
                width = int(self.cv_pic.shape[1] * self.resize_perc / 100) # new width
                height = int(self.cv_pic.shape[0] * self.resize_perc / 100) # new height
                dim = (width, height) # new dimensions
                
                self.cv_pic = cv2.resize(self.cv_pic, dim, interpolation = cv2.INTER_AREA) # resizing
                
                path = os.path.join(self.faces_path, pic) # new path of the picture
                
                cv2.imwrite(path, self.cv_pic) # save picture in the new path
                
                os.rename(path, os.path.join(self.faces_path, "rs_" + pic))
                
            except:
                print("Problem in " + pic + " ! Skip!")
                
            
            return self.cv_pic
    
        
    def face_detector(self, pic):
        
        ''' detect and crop face from picture'''
        
        if "crf_" in pic:
            print("Picture already CROPPED! Next! \n")
            pass
        
        else:
            
            path = os.path.join(self.faces_path, "rs_" + pic)
            
            try:
                faces = self.ff_detector(self.cv_pic) # list of landmarks
            
                for face in faces:
                    
                    # face coordinates
                    x, y = face.left(), face.top()
                    x1, y1 = face.right(), face.bottom()
                    
                self.cv_pic = self.cv_pic[y:y1, x:x1] # cropping

                cv2.imwrite(path, self.cv_pic) # save new cropped picture
                
                os.rename(path, os.path.join(self.faces_path, "crf_rs_" + pic)) # rename

            except:
                
                os.remove(path)
                print("no faces here! \n")
                
        
            return self.cv_pic
    
    
    def kill_bad_img(self, pic, cv_pic):
        
        '''delete pictures too small or with weird ratio'''
        
        if os.path.getsize(pic) < 1000: # byte
            print(pic + " picture too small: deleted! \n")
            os.remove(pic)
            
        else:                
            try:    
                if cv_pic.shape[1]*self.hwratio < cv_pic.shape[0] or cv_pic.shape[0]*self.hwratio < cv_pic.shape[1]: # check h/w ratio
                    print(pic + " weird ratio: deleted! \n")
                    os.remove(pic)

            except:
                print("Problem in " + pic + " ! Skip!")
            

    def file_hash(self, filename):
        
        '''take picture hash and put in a list'''
        
        with open(filename,'rb') as f: # read bytes
            file_hash = hashlib.md5(f.read()).hexdigest() # calculate hash
            self.hash_list.append(file_hash)
        
        return self.hash_list # obtain a list of the hash
    

#%%

if __name__ == '__main__': 
    
    # create istance from Google_scraper class    
    scrap = Google_scraper(max_images = 10,   # max 1000
                           color='original',  # original/bw
                           resize_perc= 300, # 100 == 100% (original size) 
                           faces_detector=False, # detect face: True/False
                           hide_in_background = False) # hide the process: True/False

    # define list of searches   
    search_list = ['squid games'] # pippo franco
    
    # call search_and_download method of the Google_scraper class on the istance
    scrap.search_and_download(search_list=search_list) 


