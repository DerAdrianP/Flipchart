package com.iot.restapi.entity;

import com.fasterxml.jackson.annotation.JsonProperty;


public class Temperature {
    @JsonProperty
    private static float temperature = 0;

    public Temperature() {
    }

    public static void setTemperature(float temperature) {
        Temperature.temperature = temperature;
    }

    public float getTemperature() {
        return temperature;
    }


    @Override
    public String toString(){
        return "Die aktuelle Temperatur beträgt: " + this.temperature + " °C";
    }
}
