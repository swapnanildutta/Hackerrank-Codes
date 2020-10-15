=begin
https://www.hackerrank.com/challenges/ruby-strings-iteration/problem
Write the method count_multibyte_char which takes a string as input and returns the number of multibyte characters (byte size > 1) in it. 
=end

def count_multibyte_char(str)
    char_count = 0
    
    str.each_char do |character|
        char_count += 1 if character.bytesize > 1
    end
    
    return char_count
end