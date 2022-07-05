using System;
using System.Collections.Generic;
using Syncfusion.XlsIO;
using System.IO;
//using System.Text.Json;
//using System.Text.Json.Serialization;
using Newtonsoft.Json;




namespace ConvertExcelToJSON
{
    class Program
    {
        static void Main(string[] args)
        {
            ExcelEngine excelEngine = new ExcelEngine();
            IApplication application = excelEngine.Excel;
            application.DefaultVersion = ExcelVersion.Xlsx;
            Stream stm = File.OpenRead("testoviy.xlsx");
            IWorkbook workbook = application.Workbooks.Open(stm);
            IWorksheet worksheet = workbook.Worksheets[0];

            ArrComp arrcomp = new ArrComp();
            arrcomp.Competition = new List<Competition>();
            int i = 2;
            while (worksheet.Range[i, 1].Value != "")
            {
                Competition comp = new Competition(worksheet.Range[i, 1].Value, worksheet.Range[i, 2].Value);
                Indicator indi = new Indicator(worksheet.Range[i, 3].Value, worksheet.Range[i, 4].Value);
                Ksp ksp = new Ksp(worksheet.Range[i, 5].Value, worksheet.Range[i, 6].Value);
                //Competition comp = new Competition(worksheet.Range[2, 1].Value, worksheet.Range[2, 2].Value);
                //Indicator indi = new Indicator(worksheet.Range[2, 3].Value, worksheet.Range[2, 4].Value);
                //Ksp ksp = new Ksp(worksheet.Range[2, 5].Value, worksheet.Range[2, 6].Value);

                //indi.Ksp = new Ksp[1];
                indi.Ksp = new List<Ksp>();
                //indi.Ksp[0] = ksp;
                indi.Ksp.Add(ksp);
                //comp.Indicator = new Indicator[1];
                comp.Indicator = new List<Indicator>();
                comp.Indicator.Add(indi);
                if (worksheet.Range[i+1, 1].Value == worksheet.Range[i, 1].Value)
                {
                    string s = worksheet.Range[i, 1].Value;
                    while (worksheet.Range[i + 1, 1].Value == s)
                    {
                        //indi2.Ksp = new List<Ksp>();
                        if (worksheet.Range[i+1, 3].Value != "")
                        {
                            Indicator indi2 = new Indicator(worksheet.Range[i+1, 3].Value, worksheet.Range[i+1, 4].Value);
                            indi2.Ksp = new List<Ksp>();
                            Ksp ksp2 = new Ksp(worksheet.Range[i+1, 5].Value, worksheet.Range[i+1, 6].Value);
                            indi2.Ksp.Add(ksp2);
                            if (worksheet.Range[i + 2, 3].Value != "") comp.Indicator.Add(indi2);
                            else
                            {

                                while (worksheet.Range[i+2, 3].Value == "")
                                {
                                    Ksp ksp3 = new Ksp(worksheet.Range[i+2, 5].Value, worksheet.Range[i+2, 6].Value);
                                    indi2.Ksp.Add(ksp3);
                                    i++;
                                }
                                comp.Indicator.Add(indi2);
                            }
                        }
                        else 
                        {
                            Ksp ksp2 = new Ksp(worksheet.Range[i + 1, 5].Value, worksheet.Range[i + 1, 6].Value);
                            indi.Ksp.Add(ksp2);
                        }
                        i++;
                    }
                    i++;
                    
                }
                //comp.Indicator[0] = indi;
                //arrcomp.Competition = new Competition[1];

                //arrcomp.Competition[0] = comp;
                arrcomp.Competition.Add(comp);
                //string json = JsonConvert.SerializeObject(arrcomp);
                //string json = JsonSerializer.Serialize(indi);
                //Console.WriteLine(json);
            }
            string json = JsonConvert.SerializeObject(arrcomp);
            //Console.WriteLine(json);
            //string json = JsonSerializer.Serialize(indi);
            stm.Close();
            //Console.WriteLine(json);
            File.WriteAllText(@"D:\code\ConvertExcelToJSON\bin\Debug\netcoreapp3.1\JSONfile.json", json);
            //Console.WriteLine(cell);
            


        }
    }


    public class ArrComp
    {
        //public Competition[] Competition { get; set; }
        public List<Competition> Competition { get; set; }

    }
    public class Competition
    {
        public string Name { get; set; }
        public string Description { get; set; }
        //public Indicator[] Indicator { get; set; }
        public List<Indicator> Indicator { get; set; }

        public Competition(string name, string desc)
        {
            Name = name;
            Description = desc;
        }
    }
    public class Indicator
    {
        public string Name { get; set; }
        public string Description { get; set; }
        //public Ksp[] Ksp { get; set; }
        public List<Ksp> Ksp { get; set; }

        public Indicator(string name, string desc)
        {
            Name = name;
            Description = desc;
        }

    }
    public class Ksp
    {
        public string Name { get; set; }
        public string Description { get; set; }

        public Ksp(string name, string desc)
        {
            Name = name;
            Description = desc;
        }
    }

}    
       
   


