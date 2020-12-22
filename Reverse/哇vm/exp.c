#include <stdio.h>
int main(){
int i;
unsigned char a16=0,a17=0;
unsigned char c[32]={0xF4,0x0A,0xF7,0x64,0x99,0x78,0x9E,0x7D,
            0xEA,0X7B,0X9E,0X7B,0X9F,0X7E,0XEB,0X71,
            0XE8,0X00,0XE8,0X07,0X98,0X19,0XF4,0X25,
            0XF3,0X21,0XA4,0X2F,0XF4,0X2F,0XA6,0X7C};
printf("9");
for(i=1;i<32;i++){
printf("%c",(c[i]^(-51)^c[i-1])+i);
}
return 0;
}
