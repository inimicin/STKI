import modules.scraping as scraper
import modules.utils as utils
from tqdm import tqdm
import json
import os

# for i in tqdm(range(88,len(utils.getKodeProdi()))):
for i in tqdm(range(0,3)):
    output_path = 'output/'
    kodeProdi = utils.getKodeProdi()[i]

    if not os.path.exists(output_path + kodeProdi  + '/'):
        os.makedirs(output_path + kodeProdi  + '/')
    
    for year in utils.getYears(kodeProdi):
       if year == '':
          year = 'NULL'

       url = f'http://repository.lppm.unila.ac.id/cgi/exportview/divisions/{kodeProdi}/{year}/JSON/{kodeProdi}_{year}.js'
       scrap_result = scraper.parsePage(scraper.getDriver(), url)
       json_content = scraper.getRawJSON(scrap_result)
       
       with open(output_path + kodeProdi  + f'/{year}.json', 'w', encoding="utf-8") as f:
        f.write(json_content)
