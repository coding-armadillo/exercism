class Lasagna
{
    // TODO: define the 'ExpectedMinutesInOven()' method
    public int ExpectedMinutesInOven()
    {
        return 40;
    }

    // TODO: define the 'RemainingMinutesInOven()' method
    public int RemainingMinutesInOven(int elapsed_bake_time)
    {
        return ExpectedMinutesInOven() - elapsed_bake_time;
    }

    // TODO: define the 'PreparationTimeInMinutes()' method
    public int PreparationTimeInMinutes(int number_of_layers)
    {
        return 2* number_of_layers;
    }

    // TODO: define the 'ElapsedTimeInMinutes()' method
    public int ElapsedTimeInMinutes(int number_of_layers, int elapsed_bake_time)
    {
         return PreparationTimeInMinutes(number_of_layers)+elapsed_bake_time;
    }
}
