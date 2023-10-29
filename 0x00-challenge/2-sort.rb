###
#
#  Sort integer arguments (ascending) 
#
###
result = []
ARGV.each do |arg|
    # Skip if not an integer
    next if arg !~ /^-?[0-9]+$/

    # Convert to integer
    i_arg = arg.to_i

    # Insert the result at the right position
    is_inserted = false
    i = 0
    l = result.size

    while !is_inserted && i < l do
        if result[i] < i_arg
            i += 1
        else
            result.insert(i, i_arg) # Corrected the insertion position
            is_inserted = true
            break
        end
    end

    result << i_arg if !is_inserted
end

puts result
