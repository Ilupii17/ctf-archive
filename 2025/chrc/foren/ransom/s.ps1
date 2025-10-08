param(
  [Parameter(Mandatory=$true)] [string]$InputFile,
  [int]$Start,
  [int]$End,
  [int]$Iterations = 200000
)

$ErrorActionPreference = "SilentlyContinue"

for ($pw = $Start; $pw -le $End; $pw++) {
    try {
        $Salt = [IO.File]::ReadAllBytes($InputFile)[0..15]
        $IV   = [IO.File]::ReadAllBytes($InputFile)[16..31]
        $Ciphertext = [IO.File]::ReadAllBytes($InputFile)[32..([IO.File]::ReadAllBytes($InputFile).Length-1)]

        $PBKDF2 = New-Object System.Security.Cryptography.Rfc2898DeriveBytes(
            [Text.Encoding]::UTF8.GetBytes($pw.ToString()),
            $Salt,
            $Iterations,
            [System.Security.Cryptography.HashAlgorithmName]::SHA256
        )

        $AES = New-Object System.Security.Cryptography.AesManaged
        $AES.Mode = [System.Security.Cryptography.CipherMode]::CBC
        $AES.Padding = [System.Security.Cryptography.PaddingMode]::PKCS7
        $AES.Key = $PBKDF2.GetBytes(32)
        $AES.IV  = $IV

        $Decryptor = $AES.CreateDecryptor()
        $PlainBytes = $Decryptor.TransformFinalBlock($Ciphertext, 0, $Ciphertext.Length)
        $PlainText  = [Text.Encoding]::UTF8.GetString($PlainBytes)

        if ($PlainText -match "CHRC|CTF|FLAG") {
            Write-Host "[+] FOUND password: $pw"
            Write-Host "[+] Plaintext:"
            Write-Output $PlainText
            break
        }
    } catch {
        # skip error
    }
}
