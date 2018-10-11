try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# FIND TESEERACT AT :
# https://github.com/tesseract-ocr/tesseract/wiki

def parseProperly(searchWord):
    # splits table to array to search
    # saving headings as 1st to  10th
    first, second, third, fourth, fifth, sixth, seventh, eight, ninth, tenth, eleven, twelve, *extraWords = searchWord.split()
    return extraWords

def searchForMoreThanOneWord(first,extrawords,arr):
    count = 0
    # -11 to compenstae for the if condtion to search through the array with text only comparison
    while count < (len(arr)-11):
        if first == arr[count + 11] :
            # print(first)
            firstLeft =arr[count - 5]
            firstTop =arr[count - 4]
            totalWidth = int(arr[count - 3])
            totalHeight = int(arr[count - 2])
            innerCount = count+23
            tempHeight = 0
            tempWidth = 0

            for x in range(len(extrawords)):
                if extrawords[x] == arr[innerCount]:

                    # print(arr[innerCount])
                    tempWidth = tempWidth+ int(arr[innerCount - 3])
                    tempHeight = int(arr[innerCount - 2])
                    if tempHeight > totalHeight:
                        totalHeight = tempHeight
                    innerCount=innerCount+12
                    if x == (len(extrawords)-1):
                        totalWidth= totalWidth+ tempWidth
                        print("condition werks")
                        return firstLeft + "," + firstTop + "," + str(totalWidth) + "," + str(totalHeight)
         #       return count number i suppose?
        count =count+ 1
    return "word is not to be seen ( inside search for 2 method)"

    # return  "method called for 2 or more words"

def searchForWord(arr,searchWord):
    first , *extraWords = searchWord.split()
    # print(first)
    # print(extraWords)
    if extraWords:
        return searchForMoreThanOneWord(first,extraWords,arr)
    # return "test"
    print("searching for 1 word word now")
    count = 0
    # -11 to compenstae for the if condtion to search through the array with text only comparison
    while count < (len(arr)-11):
        # print(arr[count])
        if first == arr[count + 11] :
            print("word found btw next word is "+ arr[count+(11+12)])
            return arr[count - 5] + "," + arr[count - 4] + "," + arr[count - 3] + "," + arr[count - 2]
            break
        #       return count number i suppose?
        count =count+ 1
    return "word is not to be seen (inside search for 1 method)"

def openImage(imagePath):
    imageFile = Image.open(imagePath)
    img = imageFile.convert('L') # convert image to black and white
    img.save('kewls.jpg')
    foundTxt = (pytesseract.image_to_data(img))
    # print(foundTxt)
    # PARSES all WORDS INTO 1 array TO EASILY get xy coordinates and size of words etc..
    arrayOFWords = parseProperly(foundTxt)
    # Function to put words array based on what line it is on
    return  arrayOFWords


def startSearch(imagePath,searchWord):
    # the actual runing of the tesseract
    # CHANGE TO INSTALL PATH OF TESSERACT
    pytesseract.pytesseract.tesseract_cmd = r'D:\Apps\Tesseract-OCR\tesseract.exe'
    print(imagePath + " " + searchWord)
    arr = openImage(imagePath)
    foundLocation = (searchForWord(arr, searchWord))
    print("nigga the words aare located at ")
    print(foundLocation)
    # TO SEND LOCATION in the format :  X,Y,width,height
    # return foundLocation



startSearch("nigga.jpg","The href attribute ")
