def every_other(array)
    array.each_with_index do |number, index|
        if index.even?
            array.each do |other_number|
                puts number + other_number
            end
        end
    end
end

every_other([10, 2])