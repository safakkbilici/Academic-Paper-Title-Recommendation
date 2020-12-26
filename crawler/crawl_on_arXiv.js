const { assert } = require('console');

main_func = async () =>{
    const puppeteer = require('puppeteer');

    
    
    var myArgs = process.argv.slice(2);
    console.log('myArgs: ', myArgs);
     
    var field_arxiv = myArgs[0];
    var from_page = myArgs[1];
    var to_page = myArgs[2];
    var last_page = from_page;

    var title = new Array();
    var abstracts = new Array();

    fetch_pages = async () => {
        const browser = await puppeteer.launch({ headless: false });
        const page = await browser.newPage();

        let i;

        for (i = from_page; i < to_page; i++) {
            try{
                await page.goto('https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=' + field_arxiv + '&terms-0-field=all&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first&start=' + i, { headless: false, timeout: 0 });
                title.push(
                    await page.evaluate(() => {
                        return document.querySelector('ol.breathe-horizontal li.arxiv-result p.title.is-5.mathjax')
                            .innerText;
                    })
                );
                abstracts.push(
                    await page.evaluate(() => {
                        return document
                            .querySelector('ol.breathe-horizontal li.arxiv-result span.abstract-full.has-text-grey-dark.mathjax')
                            .innerText.trim();
                    })
                );
                console.log('Crawler is on page : ' + i);
                
            }
            catch(err){
                console.log('ERROR ON '+ i +'. page : '+ err);
                break;
            }

        }
        
    
        last_page = i;
        //console.log(title);
        //console.log(abstracts);
        await browser.close();
    };

    await fetch_pages();


    abstract_clean = async() =>{

        let i;
        let len_abs = abstracts.length;
        for(i = 0 ; i <  len_abs; i++){
            abstracts[i] = abstracts[i].substring(0, abstracts[i].length-15);
        }
    }

    await abstract_clean();


    csv_write = async() => {
        
        const fs = require('fs')
        const csv = require('fast-csv')

        const append = (file, rows = []) => {
            const csvFile = fs.createWriteStream(file, { flags: 'a' });
            csvFile.write('\n');
            csv.writeToStream(csvFile, rows, { headers: false })
        }

        var rows = [];
        let i;
        let len_abs = abstracts.length;
        for(i = 1 ; i <  len_abs; i++){
            rows.push({input_text: abstracts[i], target_text: title[i]});
        }


        await csv.writeToStream(fs.createWriteStream(from_page +'_' + last_page +'.csv'),
            [
                { input_text: abstracts[0], target_text: title[0]  },
            ],
            { headers: true }).on('finish', () => {
                append(from_page +'_' + last_page +'.csv', rows);
            });
        console.log('Writing to csv file is done...');
        
    }

    await csv_write();

}

main_func();
