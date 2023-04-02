import { Component, OnInit } from '@angular/core';
import { Prescription } from 'src/app/models/prescription.model';
import { PrescriptionService } from 'src/app/services/prescription.service';

@Component({
  selector: 'app-prescription-list',
  templateUrl: './prescriptions-list.component.html',
  styleUrls: ['./prescriptions-list.component.css']
})


export class PrescriptionsListComponent implements OnInit {

  prescription?: any;
  prescription_type = '';
  currentPrescription: Prescription = {};
  currentIndex = -1;
  title = '';
  page = 1;
  count = 0;
  tableSize = 10;

  constructor(private prescriptionService: PrescriptionService) { 
}

  ngOnInit(): void {
    this.retrievePrescriptions();

    
  }

  
  retrievePrescriptions(): void {
    const userData = JSON.parse(localStorage.getItem('userData')|| '{}')
    console.log(userData.user_id);
    this.prescriptionService.getAll(userData.user_id)
    
      .subscribe(
        data => {
          this.prescription = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }
  
  refreshList(): void {
    this.retrievePrescriptions();
    this.currentPrescription = {};
    this.currentIndex = -1;
  }
    
  tabSize(event:any){
    this.page = event;
    //this.retrieveClients();
  }  

  tableData(event:any): void {
    this.tableSize = event.target.value;
    this.page = 1;
    this.retrievePrescriptions();
  } 

  setActiveAppointment(prescription: Prescription, index: number): void {
    this.currentPrescription =prescription;
    this.currentIndex = index;
  }

  searchPrescription(): void {
    this.currentPrescription = {};
    this.currentIndex = -1;

    this.prescriptionService.findByPrescriptionType(this.prescription_type)
      .subscribe(
        data => {
          this.prescription = data;
          this.page=1
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

}


