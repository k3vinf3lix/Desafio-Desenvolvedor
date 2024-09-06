SELECT c.cliente_id, c.razao_social, t.numero_telefone
FROM Clientes c
JOIN Estados e ON c.estado_id = e.estado_id
JOIN Telefones t ON c.cliente_id = t.cliente_id
WHERE e.sigla = 'SP';