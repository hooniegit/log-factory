package com.springboot.api.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.web.bind.annotation.*;
import java.util.Map;

import com.springboot.api.dto.MemberDto;

@RestController
@RequestMapping("/api/v1/get-api")
public class GetController {

    private final Logger LOGGER = LoggerFactory.getLogger(GetController.class);

    @GetMapping(value="/hello")
    public String getHello(){
        LOGGER.info("getHello 메서드가 호출되었습니다.");
        return "Hello, World~!";
    }

    @GetMapping(value="/name")
    public String getName(){
        LOGGER.info("getMessage 메서드가 호출되었습니다.");
        return "Name, World~!";
    }

    @GetMapping(value="/variable/{variable}")
    public String getVariable(@PathVariable String variable){
        LOGGER.info("@PathVariable을 통해 들어온 값:{}", variable);
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

    @GetMapping(value="/request/dto")
    public String getRequestDto(MemberDto memberDto){
        return memberDto.toString();
    }
}
