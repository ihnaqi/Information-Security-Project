import { Component, OnInit } from '@angular/core';
import { DoctorService } from 'src/app/services/doctor.service';
import { ActivatedRoute, Router } from '@angular/router';

import { Doctor } from 'src/app/models/doctor.model';

@Component({
  selector: 'app-doctor-details',
  templateUrl: './doctors-details.component.html',
  styleUrls: ['./doctors-details.component.css']
})

export class DoctorsDetailsComponent implements OnInit {
  
  status : any = "4";
  currentDoctor: Doctor = {
    id: '',
    // doctor_amount: 0,

    user:'',
    
  };
  message = '';
  doctors?: Doctor[];
  constructor(
    private doctorService: DoctorService,
    private route: ActivatedRoute,
    private router: Router) { }

    ngOnInit(): void {
      this.message = '';
      this.retrieveDoctors();
      this.getDoctor(this.route.snapshot.params.id);
    }
    
    
  retrieveDoctors(): void {
    this.doctorService.getAll()
      .subscribe(
        data => {
          this.doctors = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

    getDoctor(id: string): void {
      this.doctorService.get(id)
        .subscribe(
          data => {
            this.currentDoctor = data;
            console.log(data);
          },
          error => {
            console.log(error);
          });
    }
  
    updatePublished(status: boolean): void {
      const data = {
        doctor_id: this.currentDoctor.id,
        // doctor_amount: 0,
        doctor_time:'',
        doctor:'',
      };
  
      this.message = '';
  
      this.doctorService.update(this.currentDoctor.id, data)
        .subscribe(
          response => {
            console.log(response);
            this.message = response.message ? response.message : 'The status was updated successfully!';
          },
          error => {
            console.log(error);
          });
    }
  
    updateDoctor(): void {
  
      this.doctorService.update(this.currentDoctor.id, this.currentDoctor)
        .subscribe(
            
          error => {
            console.log(error);
          });
        // this.router.navigate(['/View-Doctors/'+this.currentDoctor.patient]);
          
    }
  
    deleteDoctor(): void {
      this.doctorService.delete(this.currentDoctor.id)
        .subscribe(
          response => {
       
            this.message = response.message ? response.message : 'This doctor was deleted successfully!';
            // this.router.navigate(['/View-Doctors/'+this.currentDoctor.patient]);
          },
          error => {
            console.log(error);
          });
    }
  }

