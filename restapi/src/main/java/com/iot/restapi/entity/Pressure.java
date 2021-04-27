package com.iot.restapi.entity;

public class Pressure {

    private static float pressure = 0;

    public Pressure() {
    }

    public static void setPressure(float pressure) {
        Pressure.pressure = pressure;
    }

    public float getPressure() {
        return pressure;
    }


    @Override
    public String toString(){
        return "Der aktuelle Druck beträgt: " + this.pressure + " hPA";
    }
}
