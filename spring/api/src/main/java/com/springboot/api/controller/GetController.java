package com.springboot.api.controller;

import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {

    @GetMapping(value="/hello")
    public String getHello(){
        return "Hello, World~!";
    }

    @GetMapping(value="/name")
    public String getName(){
        return "Name, World~!";
    }

    @GetMapping(value="/variable/{variable}")
    public String getVariable(@PathVariable String variable){
        return variable;
    }

    @GetMapping(value="/variable/var/{variable}")
    public String getVariableVar(@PathVariable("variable") String var){
        return var;
    }

    @GetMapping(value="/request")
    public String getRequestParam(
            @RequestParam String name,
            @RequestParam String email,
            @RequestParam String organization) {
        return name + " " + email + " " + organization;
    }

    @GetMapping(value="/request/map")
    public String getRequestMap(@RequestParam Map<String, String> param){
        StringBuilder sb = new StringBuilder();

        param.entrySet().forEach(map -> {
            sb.append(map.getKey() + " : " + map.getValue() + "\n");
        });

        return sb.toString();
    }
}
