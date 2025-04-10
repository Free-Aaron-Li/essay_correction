/*
 Copyright (c) 2025. aaron.

 This program is under the GPL-3.0 license.
 if you have not received it or the program has several bugs, please let me know:
 <communicate_aaron@outlook.com>.
 */
import JSEncrypt from 'jsencrypt/bin/jsencrypt.min'

// 密钥对生成 http://web.chacuo.net/netrsakeypair
const publicKey = `MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAu/hlJDB87a67n8QBYx97
z4oZvNccUnvAt7+gjnqmL2HvBqH8vqPsbdKPxiLHK7yWxfQRMz/GmuCiogsQUjE0
cziCcBr1rhNFLdziU7GwzXwE/r21wBqCVYxiFLErWiY65xlpFzHvpb33NF9c5QSg
vvK3iBtPpqwQqxE48H4eA21WS20mHtXugpXopB0WkFlwZtU12gMRG1P/boISAXCl
yGsyIaYgAx4WoA6a/375C0pbi5yMLrx25iBP8UrVQFdk+DqwXpWSYHWpZsbPpxiH
zlikiEwyFPsN+W6Jl9S5IPuybi5BInsl/pL6giH8VBHvPCSsBg3dBPTDctTlg1LU
QQIDAQAB`

const privateKey = `MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC7+GUkMHztrruf
xAFjH3vPihm81xxSe8C3v6COeqYvYe8Gofy+o+xt0o/GIscrvJbF9BEzP8aa4KKi
CxBSMTRzOIJwGvWuE0Ut3OJTsbDNfAT+vbXAGoJVjGIUsStaJjrnGWkXMe+lvfc0
X1zlBKC+8reIG0+mrBCrETjwfh4DbVZLbSYe1e6CleikHRaQWXBm1TXaAxEbU/9u
ghIBcKXIazIhpiADHhagDpr/fvkLSluLnIwuvHbmIE/xStVAV2T4OrBelZJgdalm
xs+nGIfOWKSITDIU+w35bomX1Lkg+7JuLkEieyX+kvqCIfxUEe88JKwGDd0E9MNy
1OWDUtRBAgMBAAECggEBAKKsVHOeVu+n0Y5xpbWwEIlK/f00uLkVinI7L+s+b8X/
3kmCNOaTnNBqcqzJek76lg1YrO4KWom8sGLGamiHVtoEZLY6TrZIzQzk5SYDWHxs
wTHo4nsPNg5tQJChx1/sR/uqPQ2q1Lg+j8rOYOl+ONMn4Pe0kxkuPfqeHAXdT4Is
RsrDdjz9yphaTPN+zX7YzDbZKxye7BPxCKTZUTi7pLm/dszU0S6+DZ6YyGt4j/Gp
KTCloyDtTZCEUWTZWbYQV0HsaFsGmoDxViK31QqgFKXC5Q7wRS7RuCpxbqwjJRj5
jDi/YYIZliCG+vYnmPbkrqmvPbt5e1Z9hFQGmBEUwnECgYEA83TmAQ2R399vofdE
RUGYijyZeVgf5NwhzBXjFWVuRnrnDiRa6bHEd3maEFjf/CKkIt8OFhf/RQvjMovZ
wQSvvWLKvDcPEK4jfkfl8rz2YSbatyQ1Pop5XxuEz/xxh/CbniCmnhfq+GiAIu4d
pXIt1eLEMR27MCZnfH4ncuNMJQUCgYEAxaenEwLG5VdkoW+zqVBZmq0M5gUvOE/7
V/vhJt/4wrthvDOV518pJxEDfjJTxnpSbSaFMPgMgruyCoBcuXm2ccHl7hBETqY9
GloqR0Iin6plb+dQK5Bcd9vAtYYqSHu6Qsq/vFjY6OkkYUCoFICrOYQjtzO0Sb2v
KEh8szZTlw0CgYEAvosGnVpeioZY274oa7/8QG1PfT5wr/FubknPEmbxmS4F+vaP
RQqCBzRgVV0J6U+/gR9s6fPcMdEs/9mfE0e0uBhDLm41V0vDsclZ+tLUTpNXaTFo
jstYVQy3tQUSYl/5nBhX77IukD9R0oTlJSEpKJa0EPEBGZ1lL3WZMH0fknUCgYEA
tareeS64ONsWdvsAGsLrWKtti42AVTXOQpQT4XNCZVls/1o6kap5XJrapwcC0Q5k
7EXXbabPeOmjPtu0XhVshyo8d48j+VX6G1p8OXqj8DThfvUQTrolA1VLzow+GNj/
3ZwUlrziwVBoS6rt0cphlj/Jw/0V3CEn+NKHKwDn25ECgYASoEuhG5veDM6fz1Wc
TWQaSXuFXqcOnv+dWGoumyKkgVy3AEqSv5V8vf/94tJzwqvllnYwHmcsiTJudTNv
7fnN8K/52YvLKq4YlOWbrGGQLXPHsP7bTZVDGwxllz0KjBj7+FzqUHe3MOqW7K9Z
2BdSAp29vZOuiqri59fbM909+g==`

// 加密
export function encrypt(txt) {
    const encryptor = new JSEncrypt()
    encryptor.setPublicKey(publicKey) // 设置公钥
    return encryptor.encrypt(txt) // 对数据进行加密
}

// 解密
export function decrypt(txt) {
    const encryptor = new JSEncrypt()
    encryptor.setPrivateKey(privateKey) // 设置私钥
    return encryptor.decrypt(txt) // 对数据进行解密
}
