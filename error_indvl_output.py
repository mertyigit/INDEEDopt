def error_indvl_output(error):
    
    """Write the moelcular property values into a file"""
       
    number_of_training_element = len(error)
    try:

        file = open("individual_error","a+") 
        file.seek(0)
            
        try:    
        
            for i in range(0, number_of_training_element):    
                    
                total_error ="{:.6f}".format(((error[i][1]-error[i][0])/error[i][2])**2)
                file.write(str(error[i][0]).rjust(12)+str(error[i][1]).rjust(12)+str(error[i][2]).rjust(12)+str(total_error).rjust(20)+"\n")
                    
        finally:
            file.close()
            
    except IOError:
            pass