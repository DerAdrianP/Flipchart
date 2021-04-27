package com.iot.restapi.controller;

import com.iot.restapi.entity.Temperature;
import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.*;

import java.awt.*;

@RestController
@RequestMapping("/temperature")
public class TemperatureController {

    Temperature currentTemp = new Temperature();

    @GetMapping
    public Temperature listTemperature(){
        return currentTemp;
    }

    @PutMapping(produces = MediaType.APPLICATION_JSON_VALUE)
    public @ResponseBody Temperature updateTemperature (@RequestBody float temperature){
        currentTemp.setTemperature(temperature);
        System.out.println("Die Temperatur wurde geändert und beträgt nun: "+temperature);
        return currentTemp;
    }
}
