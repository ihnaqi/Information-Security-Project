import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Prescription } from '../models/prescription.model';

const baseUrl = 'http://localhost:8000/api/Prescriptions';
const patientUrl = 'http://localhost:8000/api/PrescriptionsByPatient';

@Injectable({
  providedIn: 'root'
})

export class PrescriptionService {
  constructor(private http: HttpClient) { }

  getAll(id: any): Observable<Prescription[]> {
    return this.http.get<Prescription[]>(`${patientUrl}/${id}`);
  }

  get(id: any): Observable<Prescription> {
    return this.http.get(`${baseUrl}/${id}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(baseUrl, data);
  }

  update(id: any, data: any): Observable<any> {
    return this.http.put(`${baseUrl}/${id}`, data);
  }

  delete(id: any): Observable<any> {
    return this.http.delete(`${baseUrl}/${id}`);
  }

  deleteAll(): Observable<any> {
    return this.http.delete(baseUrl);
  }

  findByTitle(title: any): Observable<Prescription[]> {
    return this.http.get<Prescription[]>(`${baseUrl}?title=${title}`);
  }

  findByPrescriptionType(prescription_type: any): Observable<Prescription[]> {
    return this.http.get<Prescription[]>(`${baseUrl}?prescription_type_keyword=${prescription_type}`);
  }

}

