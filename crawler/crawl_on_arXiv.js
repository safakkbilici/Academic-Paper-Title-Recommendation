const { assert } = require('console');

main_func = async () =>{
    const puppeteer = require('puppeteer');

    
    
    var myArgs = process.argv.slice(2); 
    console.log('myArgs: ', myArgs); //parse the arguments 
      
    var field_arxiv = myArgs[0];     // first argument is crawled field like cs.cl
    var from_page = myArgs[1];       // second argument is starting index
    var to_page = myArgs[2];         // third argument is stopping index
    var last_page = from_page;

    var title = new Array();
    var abstracts = new Array();

    fetch_pages = async () => {
        const browser = await puppeteer.launch({ headless: false }); // if you do not want to open window while crawling set headless true
        const page = await browser.newPage(); 

        let i;

        for (i = from_page; i < to_page; i++) {
            try{
                //this url is taken from advanced search query of arXiv.org "https://arxiv.org/search/advanced"
                await page.goto('https://arxiv.org/search/advanced?advanced=&terms-0-operator=AND&terms-0-term=' + field_arxiv + '&terms-0-field=all&classification-physics_archives=all&classification-include_cross_list=include&date-filter_by=all_dates&date-year=&date-from_date=&date-to_date=&date-date_type=submitted_date&abstracts=show&size=200&order=-announced_date_first&start=' + i, { headless: false, timeout: 0 });
                title.push(
                    await page.evaluate(() => {
                        return document.querySelector('ol.breathe-horizontal li.arxiv-result p.title.is-5.mathjax') // select the title of paper of i.th index 
                            .innerText;
                    })
                );
                abstracts.push(
                    await page.evaluate(() => {
                        return document
                            .querySelector('ol.breathe-horizontal li.arxiv-result span.abstract-full.has-text-grey-dark.mathjax') // select the abstract of paper of i.th index 
                            .innerText.trim();
                    })
                );
                console.log('Crawler is on page : ' + i);
                
            }
            catch(err){
                console.log('ERROR ON '+ i +'. page : '+ err); // if any error accures while crawling, crawler stops and create csv file before it ends
                break;
            }

        }
        
    
        last_page = i;
        //console.log(title);
        //console.log(abstracts);
        await browser.close();
    };

    await fetch_pages();

    // Make sure do not take unwanted symbols end of the abstacts
    abstract_clean = async() =>{

        let i;
        let len_abs = abstracts.length;
        for(i = 0 ; i <  len_abs; i++){
            abstracts[i] = abstracts[i].substring(0, abstracts[i].length-15);
        }
    }

    await abstract_clean();

    //writing titles and abstracts to the csv file named "from_page + '_' + last_page + '.csv'" 
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

main_func(); // run crawler run!
