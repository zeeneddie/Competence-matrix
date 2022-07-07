using System.Collections.Generic;
using Syncfusion.XlsIO;
using System.IO;
using Newtonsoft.Json;
namespace ConvertExcelToJSON
{
    class Program
    {
        static string ModelType(string modelName)
        {
            switch (modelName[0])
            {
                case 'З':
                    return "Knowledge";
                case 'У':
                    return "Skill";
                case 'В':
                    return "Possession";
                default:
                    return "";
            }
        }
        static void Main(string[] args)
        {
            ExcelEngine excelEngine = new ExcelEngine();
            IApplication application = excelEngine.Excel;
            application.DefaultVersion = ExcelVersion.Xlsx;
            Stream stm = File.OpenRead("testoviy.xlsx");
            IWorkbook workbook = application.Workbooks.Open(stm);
            IWorksheet worksheet = workbook.Worksheets[0];
            ArrComp arrcomp = new ArrComp();
            arrcomp.children = new List<Model>();
            int i = 2;
            while (worksheet.Range[i, 1].Value != "")
            {
                Model comp = new Model(worksheet.Range[i, 1].Value, worksheet.Range[i, 2].Value, "Competence");
                Model indi = new Model(worksheet.Range[i, 3].Value, worksheet.Range[i, 4].Value, "Indicator");
                Model ksp = new Model(worksheet.Range[i, 5].Value, worksheet.Range[i, 6].Value, ModelType(worksheet.Range[i, 6].Value));
                indi.children = new List<Model>();
                indi.children.Add(ksp);
                comp.children = new List<Model>();
                comp.children.Add(indi);
                if (worksheet.Range[i + 1, 1].Value == worksheet.Range[i, 1].Value)
                {
                    string s = worksheet.Range[i, 1].Value;
                    while (worksheet.Range[i + 1, 1].Value == s)
                    {
                        if (worksheet.Range[i + 1, 3].Value != "")
                        {
                            Model indi2 = new Model(worksheet.Range[i + 1, 3].Value, worksheet.Range[i + 1, 4].Value, "Indicator");
                            indi2.children = new List<Model>();
                            Model ksp2 = new Model(worksheet.Range[i + 1, 5].Value, worksheet.Range[i + 1, 6].Value, ModelType(worksheet.Range[i + 1, 6].Value));
                            indi2.children.Add(ksp2);
                            if (worksheet.Range[i + 2, 3].Value != "") comp.children.Add(indi2);
                            else
                            {
                                while (worksheet.Range[i + 2, 3].Value == "")
                                {
                                    Model ksp3 = new Model(worksheet.Range[i + 2, 5].Value, worksheet.Range[i + 2, 6].Value, ModelType(worksheet.Range[i + 2, 6].Value));
                                    indi2.children.Add(ksp3);
                                    i++;
                                }
                                comp.children.Add(indi2);
                            }
                        }
                        else
                        {
                            Model ksp2 = new Model(worksheet.Range[i + 1, 5].Value, worksheet.Range[i + 1, 6].Value, ModelType(worksheet.Range[i + 1, 6].Value));
                            indi.children.Add(ksp2);
                        }
                        i++;
                    }
                    i++;
                }
                arrcomp.children.Add(comp);
            }
            string json = JsonConvert.SerializeObject(arrcomp);
            stm.Close();
            File.WriteAllText("JSONfile.json", json);
        }
    }
    public class ArrComp
    {
        public List<Model> children { get; set; }

    }
    public class Model
    {
        public string name { get; set; }
        public string description { get; set; }
        public string type { get; set; }
        public List<Model> children { get; set; }
        public Model(string name, string desc, string type)
        {
            this.name = name;
            description = desc;
            this.type = type;
        }
    }
}