package com.springboot.api.dto;

// dto: 레이어 간의 데이터 교환
// Key가 정해져 있고, 받아야 할 파라미터가 많은 경우
// 전달 하고자 하는 필드의 객체를 선언 <-> Controller 메서드의 쿼리 파라미터의 키와 매핑
// getter/setter 메서드 구현

public class MemberDto {

    private String name;
    private String email;
    private String organization;

    public String getName(){
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getEmail(){
        return email;
    }

    public void setEmail(String email){
        this.email = email;
    }

    public String getOrganization() {
        return organization;
    }

    public void setOrganization(String organization){
        this.organization = organization;
    }

    @Override
    public String toString() {
        return "MemberDto{" +
                "name=" + name + '\'' +
                ", email=" + email + '\'' +
                ", organization=" + organization + '\'' +
                '}';

    }

}
