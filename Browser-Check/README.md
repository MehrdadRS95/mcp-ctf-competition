# Browser Check

Players need to use a custom user agent, header, parameter, and Cookie value to access the flag. The easiest way to solve this challenge is through cURL or Burpsuite/Postman/similar tool.

## Description

The Monarchs are using a custom browser to access internal services. One of their sites performs these checks and gives back the parameters of the browser. https://host:6208.

## Question 1

Can you trick the application into thinking you are using the custom browser?

### Points

1000

### Solution

<details>
<summary>Solution</summary>

- User Agent: L33tBrow$er
- Header: L33tBrowser: ODU_CTF{6e6f742074686520666c6167}
- Parameter: SuperSecretArgument=SuperAmazing@rgumentV@lu3
- Cookie: admin = True

```bash
curl http(s)://domain:27756/?SuperSecretArgument=SuperAmazing@rgumentV@lu3 -A "L33tBrow$er" -H "L33tBrowser: ODU_CTF{6e6f742074686520666c6167}" -H "Cookie: admin=True"
```
</details>

### Flag

<details>
<summary>Flag</summary>

`ODUCTF{s1ckBr0wserBR0}`
</details>