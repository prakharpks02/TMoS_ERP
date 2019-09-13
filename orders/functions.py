def name_series_generator(input_array):
  
    output_array = []
    m = len(input_array)
    
    for j in range(m):
    
        input_name = input_array[j]
        n = len(input_name)
        output_name = ""
        p = 0
        for i in range(n):
            temp_chr = input_name[i]
            #print(p)

            if p == 0 and temp_chr.islower() :
                output_name += chr(ord(temp_chr)-32) 
                p += 1

            elif temp_chr == "_":
                output_name += " "
                p = 0

            else :
                output_name += temp_chr
                p += 1  
            
        output_array.append(output_name)
        
    return output_array