const noResults = document.getElementById("no-results");

const table = new Tabulator("#agenda-table", {

    layout: "fitColumns",

    ajaxURL: "/api/appointments",

    ajaxResponse:function(url, params, response){
        return response.data;
    },

    initialSort:[
        {
            column:"time",
            dir:"asc"
        }
    ],

    columns: [
        {
            title: "Data",
            field: "date"
        },
        {
            title: "Horário",
            field: "time"
        },
        {
            title: "Paciente",
            field: "patient_name"
        },
        {
            title: "CPF",
            field: "patient_cpf"
        },
        {
            title: "Médico",
            field: "doctor_name"
        },
        {
            title: "Especialidade",
            field: "specialty"
        },
        {
            title: "Convênio",
            field: "patient_insurance"
        },
        {
            title: "Status",
            field: "availability",

            headerFilter: "select",
            headerFilterParams: {
                values: {
                    "": "Todos",
                    "Agendada": "Agendada",
                    "Atendido": "Atendido",
                    "Cancelada": "Cancelada"
                }
        }
        },
    ]

});

const filters = ["doctor-filter", "patient-filter", "cpf-filter", "hour-filter"]

document
    .getElementById("filter-type")
    .addEventListener("change", function(){

        if(this.value){
            filters.forEach(filter => {
                el = document.getElementById(filter)
                el.hidden = true
                el.value = ""
                table.clearFilter();
            })
            document.getElementById(this.value).hidden = false
        }
        else{
            filters.forEach(filter => {
                document.getElementById(filter).hidden = true
            })
            table.clearFilter();
        }

    });

document
    .getElementById("hour-filter")
    .addEventListener("change", function(){

        if(this.value){
            table.setFilter(
                "time",
                "=",
                this.value
            );
        }
        else{
            table.clearFilter();
        }

    });

document
    .getElementById("status-filter")
    .addEventListener("change", function(){

        if(this.value){
            table.setFilter(
                "availability",
                "=",
                this.value
            );
            console.log(this.value)
        }
        else{
            table.clearFilter();
        }

    });

document
    .getElementById("doctor-filter")
    .addEventListener("input", function(){

        let value = this.value;

        if(value){

            table.setFilter(
                "doctor_name",
                "like",
                value
            );

        } else {
            table.clearFilter();
        }

    });

document
    .getElementById("patient-filter")
    .addEventListener("input", function(){

        let value = this.value;

        if(value){

            table.setFilter(
                "patient_name",
                "like",
                value
            );

        } else {
            table.clearFilter();
        }

    });

document
    .getElementById("cpf-filter")
    .addEventListener("input", function(){

        let value = this.value;

        if(value){

            table.setFilter(
                "patient_cpf",
                "starts",
                value
            );

        } else {
            table.clearFilter();
        }

    });



table.on("dataFiltered", function(filters, rows){

    if(rows.length === 0){
        noResults.hidden = false;
    } else {
        noResults.hidden = true;
    }

});