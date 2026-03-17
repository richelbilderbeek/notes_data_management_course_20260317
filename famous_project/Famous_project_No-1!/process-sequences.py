import vcf
v = vcf.Reader(filename='genotypes.vcf.gz')
 
print('Variant Level information')
infos = v.infos
for info in infos:
   print(info)
 
print('Sample Level information')
fmts = v.formats
for fmt in fmts:
   print(fmt)