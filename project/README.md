**Car Identification Convolutional Neural Network**


This project implements a number of Convolutional Neural Networks (CNNs) that identify a car's model from a picture of the car.  


The modules of code for this project:\
utilityFunctions.py: contains evaluation and data handling functions\
architectures.py: contains functions that define the architecture options\
runFunctions.py: contains functions that control the training of the model\
main.py: allows the code to run


To run the code:
1. Download the devkit and the tarball of both testing and training images from https://ai.stanford.edu/~jkrause/cars/car_dataset.html
2. Untar the images and the devkit
3. Change the file paths in main to match the paths that you used.
4. Run main.py with the process_data argument as true and the validation directory as car_test
5. Delete most of the folders, leaving only the following cars
    1. Aston Martin V8 Vantage Coupe 2012 
    2. Audi R8 Coupe 2012
    3. Audi TT RS Coupe 2012
    4. Bentley Mulsanne Sedan 2011
    5. BMW M3 Coupe 2012
    6. Bugatti Veyron 16.4 Coupe 2009
    7. Cadillac CTS-V Sedan 2012
    8. Chevrolet Corvette ZR1 2012
    9. Dodge Challenger SRT8 2011
    10. Ferrari 458 Italia Coupe 2012
    11. Ford GT Coupe 2006
    12. Jeep Grand Cherokee SUV 2012
    13. Jeep Wrangler SUV 2012
    14. Lamborghini Reventon Coupe 2008
    15. Land Rover Range Rover SUV 2012
    16. Porsche Panamera Sedan 2012
    17. Tesla Model S Sedan 2012
    18. Toyota 4Runner SUV 2012
    19. Volkswagen Golf Hatchback 2012
    20. Volvo C30 Hatchback 2012
    
6. Create a new folder called car_val and create one folder for each of the 20 cars listed above, named exactly the same way.
   Change the name of the validation directory back to car_val
7. Go into the test folder, and move the first 10 images into the corresponding training folder and the next 15 into the 
   corresponding folder in the validation folder.
8. Run main.py to experiment, changing arguments as necessary

Code for this work was drawn from: https://github.com/michalgdak/car-recognition

