package com.iot.restapi.controller;

import com.iot.restapi.entity.Pressure;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class PressureController {

    Pressure currentPress = new Pressure();

    @RequestMapping("/pressure")
    public String listPressure(){
        return currentPress.toString();
    }

    @PostMapping("/pressure")
    public void postPressure(float pressure){
        currentPress.setPressure(pressure);
        System.out.println("Der Druck wurde geändert und beträgt nun: "+pressure);
    }

}


