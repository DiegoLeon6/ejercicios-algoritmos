valorSalario = 1623500
print ("Teniendo en cuenta que el SMLV (con aux. de transporte) es de: ", valorSalario)

aporteSalud = 0.04 * valorSalario
print ("Teniendo en cuenta que su aporte a salud es del 4% sobre su salario: ", aporteSalud)

aportePension = 0.04 * valorSalario
print ("Teniendo en cuenta que su aporte a pension es del 4% sobre su salario: ", aportePension)

aporteSeguridadSocial = aportePension + aporteSalud

print ("Por lo tanto su aporte de seguridad social (Salud + Pension) corresponde a: ", aporteSeguridadSocial)

salarioNeto = valorSalario - aporteSeguridadSocial

print ("su salario neto base corresponde a: ", salarioNeto)