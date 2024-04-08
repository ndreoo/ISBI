
package com.company.model;

import java.time.LocalDateTime;
import javax.persistence.Column;
import javax.persistence.Convert;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Lob;
import javax.persistence.NamedQueries;
import javax.persistence.NamedQuery;
import javax.persistence.Table;
import javax.persistence.Version;
import org.hibernate.annotations.GenericGenerator;
import org.hibernate.annotations.Parameter;


/**
 * 
 */
@javax.persistence.Entity(name = "Tang")
@Table(name = "TANG")
@NamedQueries({
    @NamedQuery(name = "Tang.findByPersistenceId", query = "SELECT t\nFROM Tang t\nWHERE t.persistenceId= :persistenceId\n"),
    @NamedQuery(name = "Tang.findByDatet", query = "SELECT t\nFROM Tang t\nWHERE t.datet= :datet\nORDER BY t.persistenceId"),
    @NamedQuery(name = "Tang.findByStazione", query = "SELECT t\nFROM Tang t\nWHERE t.stazione= :stazione\nORDER BY t.persistenceId"),
    @NamedQuery(name = "Tang.findByTraffico", query = "SELECT t\nFROM Tang t\nWHERE t.traffico= :traffico\nORDER BY t.persistenceId"),
    @NamedQuery(name = "Tang.findByCausa", query = "SELECT t\nFROM Tang t\nWHERE t.causa= :causa\nORDER BY t.persistenceId"),
    @NamedQuery(name = "Tang.findByOpen_bars", query = "SELECT t\nFROM Tang t\nWHERE t.open_bars= :open_bars\nORDER BY t.persistenceId"),
    @NamedQuery(name = "Tang.findByAccept", query = "SELECT t\nFROM Tang t\nWHERE t.accept= :accept\nORDER BY t.persistenceId"),
    @NamedQuery(name = "Tang.find", query = "SELECT t\nFROM Tang t\nORDER BY t.persistenceId"),
    @NamedQuery(name = "Tang.countForFindByDatet", query = "SELECT COUNT(t)\nFROM Tang t\nWHERE t.datet= :datet\n"),
    @NamedQuery(name = "Tang.countForFindByStazione", query = "SELECT COUNT(t)\nFROM Tang t\nWHERE t.stazione= :stazione\n"),
    @NamedQuery(name = "Tang.countForFindByTraffico", query = "SELECT COUNT(t)\nFROM Tang t\nWHERE t.traffico= :traffico\n"),
    @NamedQuery(name = "Tang.countForFindByCausa", query = "SELECT COUNT(t)\nFROM Tang t\nWHERE t.causa= :causa\n"),
    @NamedQuery(name = "Tang.countForFindByOpen_bars", query = "SELECT COUNT(t)\nFROM Tang t\nWHERE t.open_bars= :open_bars\n"),
    @NamedQuery(name = "Tang.countForFindByAccept", query = "SELECT COUNT(t)\nFROM Tang t\nWHERE t.accept= :accept\n"),
    @NamedQuery(name = "Tang.countForFind", query = "SELECT COUNT(t)\nFROM Tang t\n")
})
public class Tang implements org.bonitasoft.engine.bdm.Entity
{

    @Id
    @GeneratedValue(generator = "default_bonita_seq_generator")
    @GenericGenerator(name = "default_bonita_seq_generator", strategy = "org.hibernate.id.enhanced.SequenceStyleGenerator", parameters = {
        @Parameter(name = "sequence_name", value = "hibernate_sequence")
    })
    private Long persistenceId;
    @Version
    private Long persistenceVersion;
    @Column(name = "DATET", nullable = true, length = 30)
    @Convert(converter = org.bonitasoft.engine.business.data.generator.DateAndTimeConverter.class)
    private LocalDateTime datet;
    @Column(name = "STAZIONE", nullable = true, length = 255)
    private String stazione;
    @Column(name = "TRAFFICO", nullable = true)
    private Boolean traffico;
    @Column(name = "CAUSA", nullable = true)
    @Lob
    private String causa;
    @Column(name = "OPEN_BARS", nullable = true)
    private Boolean open_bars;
    @Column(name = "ACCEPT", nullable = true)
    private Boolean accept;

    public Tang() {
    }

    public void setPersistenceId(Long persistenceId) {
        this.persistenceId = persistenceId;
    }

    public Long getPersistenceId() {
        return persistenceId;
    }

    public void setPersistenceVersion(Long persistenceVersion) {
        this.persistenceVersion = persistenceVersion;
    }

    public Long getPersistenceVersion() {
        return persistenceVersion;
    }

    public void setDatet(LocalDateTime datet) {
        this.datet = datet;
    }

    public LocalDateTime getDatet() {
        return datet;
    }

    public void setStazione(String stazione) {
        this.stazione = stazione;
    }

    public String getStazione() {
        return stazione;
    }

    public void setTraffico(Boolean traffico) {
        this.traffico = traffico;
    }

    public Boolean isTraffico() {
        return traffico;
    }

    public void setCausa(String causa) {
        this.causa = causa;
    }

    public String getCausa() {
        return causa;
    }

    public void setOpen_bars(Boolean open_bars) {
        this.open_bars = open_bars;
    }

    public Boolean isOpen_bars() {
        return open_bars;
    }

    public void setAccept(Boolean accept) {
        this.accept = accept;
    }

    public Boolean isAccept() {
        return accept;
    }

}
