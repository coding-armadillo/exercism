local leap_year = function(number)
  if (number % 4 == 0 and number % 100 ~= 0) or (number % 400 == 0) then
    return true
  else
    return false
  end
end

return leap_year
