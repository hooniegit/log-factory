package com.springboot.api.controller;

import com.springboot.api.dto.MemberDto;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import java.util.Map;

// RestController 어노테이션 지정 시 ResponseBody 생략 가능
// ResponseBody 어노테이션은 자동으로 값을 JSON으로 변환해 전달
@RestController
@RequestMapping("/api/v1/put-api")
public class PutController {

    @PutMapping(value = "/member")
    public String putMember(@RequestBody Map<String, Object> putData){
        StringBuilder sb = new StringBuilder();

        putData.entrySet().forEach(map -> {
            sb.append(map.getKey() + ":" + map.getValue() + "\n");
        });

        return sb.toString();
    }

    @PutMapping(value = "/member/dto")
    public String putMemberDto(@RequestBody MemberDto memberDto){
        return memberDto.toString();
    }

    // text/plain 대신 application/json 형식으로 전달
    @PutMapping(value = "/pub/member/dto")
    public MemberDto pubMemberDto(@RequestBody MemberDto memberDto){
        return memberDto;
    }

}
