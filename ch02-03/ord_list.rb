def linear_search(array, search_value)
    array.each_with_index do |element, index|
        if element == search_value
            return index
        elsif element > search_value
            break
        end
    end

    return nil
end

print(chars.ascii_only?(),"\n")
p linear_search([3, 17, 75, 80, 202], 202)
